# SMEsPlus ENTERPRISE SUITE
## GMVQ — G03 MASTER_DATA / uom Module Adversarial MVQ Bank

**Document ID:** GMVQ-G03-UOM-MVQ50-V1.00
**Group:** G03 MASTER_DATA
**Module Metadata:** `uom`
**Wave:** W1
**Author Cell:** TEAM 19 (Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50
**Lane A / Lane B:** NOT STARTED for this module until rolling batch freeze is recorded

## Purpose

This bank supplies the module-specific (MVQ) questions for `uom` — units of measure, categories
of unit, and conversion between them — required alongside the 35 Standard Questions before
blind two-lane study can begin for this module.

`uom` is a quiet, high-damage master-data module: a conversion defect corrupts quantity, cost,
valuation and tax simultaneously, and typically surfaces only months later when a reconciliation
or audit finally traces a discrepancy back to a rounding or factor-change event. This bank
therefore concentrates depth on one module rather than breadth across several, per programme
instruction for this authoring pass.

Coverage deliberately spans: conversion-factor precision and round-trip integrity; rounding
placement and residual accumulation; factor and category mutation after transactions or stock
exist; multi-unit precedence (purchase/stock/sales); document lifecycle across units (order,
delivery, invoice, return); zero/negative/extreme-magnitude quantities; archival and deletion
semantics; per-company and per-tenant configuration isolation; import/integration boundary
behaviour; output fidelity; auditability of the factor in force at posting time; concurrency;
permission boundaries on configuration; cross-module (accounting, tax) consistency; and
optional-behaviour reachability.

The question text is source-neutral. It does not name any vendor or product, any technical
identifier (model, table, field, method, XML ID, API path), or the module's own metadata name —
`uom` appears only in the `MODULE:` field of each question block, never in question text.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` — a concrete result that
  would prove the paired `HYPOTHESIS` wrong, not a restatement of it.
- No padding: each of the 50 questions tests a materially distinct hypothesis: no two share a
  disconfirming observation or reduce to a variation of another question in this bank.
- `LAYER: BASE` marks questions about unit/category/factor definition and configuration.
  `LAYER: PROCESS` marks questions about behaviour during a live transaction or document
  lifecycle. Both layers exist for this module and are tagged throughout.
- Questions are not evidence. A later ANSWERED state requires an actual artifact/observation
  from the relevant lane.
- `MODULE + QID` is a Research Evidence Join Key only. No coverage or compliance status is
  derived from the existence of a question.
- This document is PREPARED ONLY / NOT FROZEN. It carries no Boss approval and authorizes no
  merge, release, or gate closure.

## G03-UOM-Q001

```yaml
QID: G03-UOM-Q001
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Converting a quantity from one unit to a second unit in the same category and then back to
  the first unit returns a value within a defined, documented tolerance of the original —
  a round trip does not silently accumulate drift.
WHY_IT_MATTERS: >
  A round trip that does not close corrupts every downstream quantity, cost and valuation that
  passes through more than one unit, and the corruption compounds with every additional hop.
DISCONFIRMING_OBSERVATION: >
  Converting a known quantity out to a second unit and back to the first produces a value that
  differs from the original by more than the documented tolerance, with no rounding rule that
  accounts for the gap.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Two units in one category with a non-trivial (non-integer-friendly) conversion factor between
  them; convert a fixed quantity out and back and compare to the original within the stated
  tolerance.
```

## G03-UOM-Q002

```yaml
QID: G03-UOM-Q002
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A unit category has exactly one reference unit at any point in time, and no business process
  ever treats two units of the same category as simultaneously authoritative.
WHY_IT_MATTERS: >
  Two candidate reference points in one category make every conversion within it ambiguous,
  because there is no longer one fixed basis to convert through.
DISCONFIRMING_OBSERVATION: >
  Two different units of the same category are each treated as the conversion basis by different
  parts of the system at the same point in time, producing two different converted results for
  the same source quantity.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Inspect a category with three or more units and trace, for two independent consuming
  processes, which unit each treats as the basis for conversion.
```

## G03-UOM-Q003

```yaml
QID: G03-UOM-Q003
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  The factor used to convert from a smaller unit to a larger one is the true mathematical
  inverse of the factor used to convert the other way, not two independently stored values that
  can silently diverge.
WHY_IT_MATTERS: >
  If the two directions are not true inverses, the direction in which a given transaction
  happens to be entered silently changes its recorded quantity.
DISCONFIRMING_OBSERVATION: >
  Converting a fixed quantity from unit A to unit B, then computing what quantity of A that
  should represent using the reverse-direction factor, yields two different numbers for the
  same physical quantity.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  A category with a defined forward and reverse conversion factor between two units; compute
  both directions independently and compare.
```

## G03-UOM-Q004

```yaml
QID: G03-UOM-Q004
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Quantity rounding is applied according to one defined rule at each of line level, document
  level and stock/valuation level, and the three levels do not silently apply different or
  undocumented rounding behaviour to the same underlying quantity.
WHY_IT_MATTERS: >
  Inconsistent rounding between levels means the same physical movement can be represented by
  three different numbers depending only on which layer of the system is asked.
DISCONFIRMING_OBSERVATION: >
  The same converted quantity, read from the document line, the document total, and the
  stock/valuation record, disagrees by more than the documented rounding rule for that level
  would allow.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A transaction whose conversion factor produces a non-terminating or non-obvious decimal;
  compare the stored quantity at line, document and stock/valuation level.
```

## G03-UOM-Q005

```yaml
QID: G03-UOM-Q005
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Summing converted quantities across many lines of one document does not accumulate a rounding
  residual larger than the tolerance defined for a single conversion — the error does not grow
  with the number of lines.
WHY_IT_MATTERS: >
  A residual that scales with line count silently worsens as documents grow larger, so it is
  most dangerous exactly where the business relies on it most.
DISCONFIRMING_OBSERVATION: >
  A document with many lines converted through the same non-trivial factor shows a total
  quantity or value discrepancy, against an independently computed reference total, larger than
  the single-conversion tolerance multiplied by a documented, bounded allowance.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Build a document with a large number of lines sharing one non-trivial conversion factor and
  compare the summed converted total against an independently computed reference.
```

## G03-UOM-Q006

```yaml
QID: G03-UOM-Q006
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Changing a unit's or a category's conversion factor after transactions already exist does not
  retroactively alter the quantity or value already recorded on those earlier transactions.
WHY_IT_MATTERS: >
  Silent restatement of posted history on a routine configuration edit destroys the reliability
  of every closed period that used the old factor.
DISCONFIRMING_OBSERVATION: >
  After changing a conversion factor, re-reading a transaction posted under the old factor shows
  a quantity or value different from what was recorded at posting time, with no explicit
  restatement action having been taken.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post a transaction using a known factor, change the factor, then re-read the original
  transaction's stored quantity and value.
```

## G03-UOM-Q007

```yaml
QID: G03-UOM-Q007
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A report or valuation that recomputes historical figures after a conversion-factor change
  reproduces the value that was true at the time each original transaction was posted, not the
  value implied by the currently active factor.
WHY_IT_MATTERS: >
  A recomputation that silently uses today's factor for yesterday's transaction fabricates a
  financial history that never actually occurred.
DISCONFIRMING_OBSERVATION: >
  A historical report re-run after a factor change produces a different figure for an already-
  posted period than the figure that period showed before the factor changed, with no explicit
  restatement authorized.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Capture a historical report figure, change the relevant conversion factor, then re-run the
  same historical report and compare.
```

## G03-UOM-Q008

```yaml
QID: G03-UOM-Q008
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Changing the reference unit of a category that already has on-hand quantity recorded in other
  units of that category does not silently reinterpret or restate the existing stock quantity.
WHY_IT_MATTERS: >
  Reassigning the basis unit under live stock can invisibly multiply or divide every existing
  balance in that category by the ratio between old and new reference units.
DISCONFIRMING_OBSERVATION: >
  After the reference unit of a category is changed, an existing on-hand balance expressed in a
  non-reference unit of that category reads as a different quantity than it did immediately
  before the change, with no explicit conversion action recorded.
EXPECTED_SURFACE: S1,S2,S6,S7
PRECONDITIONS: >
  A category with on-hand stock in more than one of its units; change the category's reference
  unit and compare each unit's reported on-hand quantity before and after.
```

## G03-UOM-Q009

```yaml
QID: G03-UOM-Q009
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Moving a unit from one category to another, while open (unfulfilled or unposted) documents
  still reference that unit, is either blocked with a clear reason or produces a defined,
  visible consequence on those documents — not a silent, undetected break in their conversion
  basis.
WHY_IT_MATTERS: >
  A unit that quietly changes which category it converts within invalidates every open
  document's pending conversion without any signal to the people relying on it.
DISCONFIRMING_OBSERVATION: >
  A unit is moved to a different category while an open document referencing it exists, and that
  document's conversion behaviour changes with no error, warning, or recorded consequence.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  An open document expressed in a unit; reassign that unit to a different category and observe
  the document's conversion behaviour and any warning raised.
```

## G03-UOM-Q010

```yaml
QID: G03-UOM-Q010
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When a document is captured in one unit but fulfilled, invoiced, or valued in a different
  unit of the same category, the transaction records explicitly which unit and quantity the
  accounting ledger actually recognizes.
WHY_IT_MATTERS: >
  Without an explicit, retrievable answer to "which unit did the ledger use," reconciling a
  document against its own accounting impact becomes guesswork.
DISCONFIRMING_OBSERVATION: >
  A document captured in one unit and posted to the ledger in a different unit provides no
  retrievable record of which unit and quantity the posting actually used, or two different
  retrieval paths disagree on the answer.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  A document entered in one unit, fulfilled or invoiced in a different unit of the same
  category; inspect the posted accounting record for the unit and quantity it recognizes.
```
## G03-UOM-Q011

```yaml
QID: G03-UOM-Q011
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When a purchasing unit, a stock-keeping unit and a selling unit differ on the same record,
  there is one documented, retrievable precedence for which unit a given downstream process
  (fulfilment, costing) uses by default when none is explicitly specified on the transaction.
WHY_IT_MATTERS: >
  Without a documented precedence, three people can each reasonably expect a different default
  unit, and the one the system actually applies becomes undiscoverable except by trial.
DISCONFIRMING_OBSERVATION: >
  Two downstream processes that both consult the same record's unit configuration, with no unit
  explicitly specified on the transaction, resolve to two different default units.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  A record configured with distinct purchasing, stock and selling units; trigger fulfilment and
  costing without specifying a transaction-level unit and compare each process's resolved unit.
```

## G03-UOM-Q012

```yaml
QID: G03-UOM-Q012
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A unit configured to require whole-number quantities rejects or blocks a fractional quantity
  entered against it, rather than silently truncating, rounding, or storing the fractional value
  as entered.
WHY_IT_MATTERS: >
  A whole-only unit that silently accepts a fraction misrepresents what was actually counted or
  handled, in a way that is invisible until a physical recount disagrees with the record.
DISCONFIRMING_OBSERVATION: >
  A quantity with a non-zero fractional part is entered against a unit configured as whole-number
  only, and the value is stored or processed as entered rather than rejected or blocked.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  A unit configured to disallow fractional quantities; attempt to enter a fractional quantity
  against it through a normal supported entry path.
```

## G03-UOM-Q013

```yaml
QID: G03-UOM-Q013
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A unit that explicitly allows fractional quantities preserves the precision actually entered
  through conversion and storage, rather than silently coercing it to a whole number at some
  point in the pipeline.
WHY_IT_MATTERS: >
  Silent coercion of a deliberately fractional quantity on a unit meant to support it loses real
  information about what was actually transacted.
DISCONFIRMING_OBSERVATION: >
  A fractional quantity entered against a unit that explicitly permits fractions is stored,
  converted, or reported as a whole number anywhere along its lifecycle without an explicit
  rounding rule that accounts for the change.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A unit configured to allow fractional quantities; enter a fractional quantity and trace it
  through storage, conversion, and reporting.
```

## G03-UOM-Q014

```yaml
QID: G03-UOM-Q014
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A document line or stock movement carrying a zero quantity is handled by one consistent,
  documented rule regardless of which unit of a category it happens to be expressed in.
WHY_IT_MATTERS: >
  A zero-quantity rule that depends on the chosen unit means the same non-event can be accepted
  or rejected purely based on an incidental unit choice.
DISCONFIRMING_OBSERVATION: >
  A zero-quantity line or movement is accepted when expressed in one unit of a category but
  rejected, or handled differently, when the identical zero quantity is expressed in another
  unit of the same category.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt a zero-quantity entry expressed in two different units of the same category through
  the same entry path and compare the outcomes.
```

## G03-UOM-Q015

```yaml
QID: G03-UOM-Q015
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A negative quantity, such as one representing a return or a correction, converts through a
  category's factor using the same rule as a positive quantity, including consistent sign
  preservation, rather than a special-cased or inconsistent path.
WHY_IT_MATTERS: >
  A sign-handling defect in conversion silently flips a return into an addition, or an addition
  into a return, in exactly the cases hardest to notice at a glance.
DISCONFIRMING_OBSERVATION: >
  Converting a negative quantity between two units of a category yields a result whose magnitude
  does not match the magnitude produced by converting the equivalent positive quantity, or whose
  sign is lost or altered.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Convert a fixed positive quantity and its negative counterpart through the same non-trivial
  factor and compare magnitude and sign.
```

## G03-UOM-Q016

```yaml
QID: G03-UOM-Q016
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A very large quantity converted between two units of a category does not overflow, silently
  truncate, or lose precision relative to the same conversion performed at an ordinary
  magnitude.
WHY_IT_MATTERS: >
  A precision or overflow defect that only appears at scale is invisible in routine testing and
  surfaces first on the business's largest, most consequential transactions.
DISCONFIRMING_OBSERVATION: >
  Converting a very large quantity produces a result whose relative precision (error as a
  fraction of the value) is measurably worse than the same conversion performed on an ordinary-
  sized quantity through the same factor.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Convert a quantity several orders of magnitude larger than typical usage through a non-trivial
  factor and compare relative precision against an ordinary-magnitude conversion.
```

## G03-UOM-Q017

```yaml
QID: G03-UOM-Q017
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a document is fulfilled across more than one partial delivery and the delivered unit
  differs from the ordered unit, the running calculation of quantity remaining stays correct,
  within tolerance, across every partial delivery.
WHY_IT_MATTERS: >
  A remaining-quantity defect across unit boundaries causes a document to appear open when it is
  actually complete, or closed while stock is still owed.
DISCONFIRMING_OBSERVATION: >
  After two or more partial deliveries in a unit different from the order's unit, the document's
  reported quantity remaining, converted to a common basis, disagrees with the order quantity
  minus the sum of deliveries by more than the documented tolerance.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  An order in one unit fulfilled through at least two partial deliveries in a different unit of
  the same category; track quantity remaining after each delivery.
```

## G03-UOM-Q018

```yaml
QID: G03-UOM-Q018
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When invoicing occurs in installments and the invoiced unit differs from the ordered or
  delivered unit, the total invoiced quantity, once converted to a common basis, matches what
  was actually delivered.
WHY_IT_MATTERS: >
  A mismatch here means the business can bill for more or less than it actually shipped without
  any single figure ever looking obviously wrong.
DISCONFIRMING_OBSERVATION: >
  The sum of installment-invoiced quantities, converted to a common basis, differs from the sum
  of delivered quantities converted to the same basis, by more than the documented tolerance,
  with no pending-invoice amount left to explain the gap.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A document delivered in one unit and invoiced across multiple installments in a different
  unit; compare total invoiced versus total delivered on a common basis.
```

## G03-UOM-Q019

```yaml
QID: G03-UOM-Q019
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A return or reversal captured in a unit different from the original transaction's unit
  produces the same net quantity impact, within tolerance, as it would if captured in the
  original unit.
WHY_IT_MATTERS: >
  A return that nets to a different quantity than the sale it reverses, purely because of a unit
  choice, leaves a residual balance that a reconciliation can never fully explain.
DISCONFIRMING_OBSERVATION: >
  A full return of a transaction, captured in a unit different from the original, leaves a net
  non-zero quantity or valuation impact greater than the documented rounding tolerance.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A transaction posted in one unit; fully return it using a different unit of the same category
  and check the net quantity and value impact.
```

## G03-UOM-Q020

```yaml
QID: G03-UOM-Q020
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Archiving or deactivating a unit that is still referenced by open (unposted or unfulfilled)
  documents, or by on-hand stock, is either blocked with a clear reason or produces a defined,
  visible consequence — not a silent broken reference on those documents or that stock.
WHY_IT_MATTERS: >
  A silently broken unit reference on live, open business means the next action taken against
  that document or stock record can fail or misbehave with no warning tracing back to the cause.
DISCONFIRMING_OBSERVATION: >
  A unit still referenced by an open document or by on-hand stock is successfully archived or
  deactivated with no block and no recorded warning, and the referencing document or stock
  record subsequently behaves incorrectly or becomes unreadable.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  A unit referenced by at least one open document and by on-hand stock; attempt to archive or
  deactivate it and observe the outcome and any warning.
```
## G03-UOM-Q021

```yaml
QID: G03-UOM-Q021
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Archiving a unit that has no open references, but does have posted historical transactions,
  leaves those historical transactions fully readable and correctly valued after the archival.
WHY_IT_MATTERS: >
  If archival degrades historical readability, the routine act of retiring an old unit quietly
  damages the audit trail of every transaction that ever used it.
DISCONFIRMING_OBSERVATION: >
  After a unit with only historical (no open) references is archived, a previously posted
  transaction using that unit becomes unreadable, misvalued, or displays a different quantity
  than it did before the archival.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  A unit with posted historical transactions and no open references; archive it and re-read the
  historical transactions.
```

## G03-UOM-Q022

```yaml
QID: G03-UOM-Q022
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Two companies (or tenants) sharing the same unit category are each able to hold their own
  rounding or precision configuration for it without one company's setting silently affecting
  another company's stored data.
WHY_IT_MATTERS: >
  Cross-company bleed on a rounding setting means one business unit's configuration change
  silently rewrites how another, unrelated business unit's transactions are stored.
DISCONFIRMING_OBSERVATION: >
  Changing a rounding or precision setting for a shared unit category under one company changes
  the stored or displayed quantity of a transaction belonging to a different company.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Two companies sharing one unit category, each with an existing transaction in it; change one
  company's rounding/precision configuration and check the other company's transaction.
```

## G03-UOM-Q023

```yaml
QID: G03-UOM-Q023
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A single business document that spans more than one company or branch resolves to one
  unambiguous unit configuration for its conversion, rather than drawing two conflicting
  configurations from each side.
WHY_IT_MATTERS: >
  Two live configurations feeding one conversion means the converted quantity on a cross-company
  document depends on which side of the boundary happened to compute it.
DISCONFIRMING_OBSERVATION: >
  A cross-company or cross-branch document produces two different converted quantities for the
  same line, depending on which company's context is used to read or recompute it.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  A document spanning two companies with potentially different unit configuration; read its
  converted quantity from each company's context and compare.
```

## G03-UOM-Q024

```yaml
QID: G03-UOM-Q024
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  An inbound integration or import that references a unit code not present in the system is
  rejected with a specific, attributable error, rather than silently mapped to a default or
  nearest-match unit.
WHY_IT_MATTERS: >
  A silent fallback to a default unit on an unrecognized code turns a data-quality problem into
  a wrong-quantity transaction with no error to alert anyone.
DISCONFIRMING_OBSERVATION: >
  An import or integration record referencing a unit code that does not exist in the system is
  accepted and processed using some other unit, with no rejection or specific error raised.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  An inbound import or integration payload referencing a unit code that has no matching
  configured unit; submit it and observe the outcome.
```

## G03-UOM-Q025

```yaml
QID: G03-UOM-Q025
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  An inbound integration or import that references a unit label matching more than one
  configured unit resolves deterministically to one documented choice, or is rejected — it does
  not pick arbitrarily among the candidates.
WHY_IT_MATTERS: >
  Arbitrary resolution among ambiguous unit candidates means the same import file can produce a
  different converted quantity on different runs.
DISCONFIRMING_OBSERVATION: >
  Submitting the same ambiguous unit label through the same import or integration path more than
  once resolves to a different matching unit on different occasions, with no documented
  precedence rule cited.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Configure two units whose labels could plausibly match one ambiguous imported label; submit
  the same import repeatedly and compare which unit is resolved each time.
```

## G03-UOM-Q026

```yaml
QID: G03-UOM-Q026
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The unit and quantity shown on a printed or exported copy of a document match exactly the unit
  and quantity that are stored and used for downstream valuation — no silent re-conversion
  happens only at output time.
WHY_IT_MATTERS: >
  A document that reads differently on paper than it is valued in the ledger destroys the
  evidentiary value of the printed record for any dispute or audit.
DISCONFIRMING_OBSERVATION: >
  A printed or exported copy of a document shows a unit or quantity that differs from the value
  stored and used for its accounting valuation, with no annotation explaining the difference.
EXPECTED_SURFACE: S1,S2,S3
PRECONDITIONS: >
  A posted document with a defined stored unit and quantity; generate its printed or exported
  form and compare against the stored record.
```

## G03-UOM-Q027

```yaml
QID: G03-UOM-Q027
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  For any posted transaction, the specific conversion factor that was applied at the time of
  posting can be reconstructed later, even after the category's or unit's factor has since been
  changed.
WHY_IT_MATTERS: >
  Without a reconstructable factor-in-force, no one can ever prove after the fact whether a
  historical transaction was correctly converted, which defeats any later audit or dispute.
DISCONFIRMING_OBSERVATION: >
  After a conversion factor has been changed, there is no way to retrieve or reconstruct which
  factor value was actually in force when an earlier transaction was posted.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Post a transaction under a known factor, change the factor, then attempt to reconstruct the
  factor that was in force at the original posting time.
```

## G03-UOM-Q028

```yaml
QID: G03-UOM-Q028
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  A change to a conversion factor is itself recorded as a discrete, attributable event — who
  changed it, when, the old value and the new value — rather than merely overwritten in place
  with no trace.
WHY_IT_MATTERS: >
  An untraceable factor change means a governance review can never establish when or by whom a
  potentially costly conversion error was introduced.
DISCONFIRMING_OBSERVATION: >
  A conversion factor is changed and no attributable record (actor, timestamp, old value, new
  value) of that change can be retrieved afterward.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Change a conversion factor through a normal supported path and attempt to retrieve a record of
  that specific change afterward.
```

## G03-UOM-Q029

```yaml
QID: G03-UOM-Q029
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A transaction being entered while its unit's conversion factor is being edited concurrently by
  another user or process ends up with one deterministic, attributable factor applied — not a
  race-dependent outcome that varies by timing alone.
WHY_IT_MATTERS: >
  A race between editing a factor and posting a transaction that uses it can silently apply
  either the old or the new factor by chance, with no way to later prove which one was used.
DISCONFIRMING_OBSERVATION: >
  Repeating the same overlapping sequence of a factor edit and a transaction post produces a
  different applied factor on different runs, with no ordering or locking rule that explains
  which one should have won.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Arrange a transaction post to overlap in time with a conversion-factor edit on the same unit,
  repeated across several runs, and compare which factor was applied each time.
```

## G03-UOM-Q030

```yaml
QID: G03-UOM-Q030
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  When a record does not explicitly specify a unit, the default unit the system applies is
  deterministic and traceable to a defined configuration setting, rather than an unexplained or
  inconsistent fallback.
WHY_IT_MATTERS: >
  An untraceable default unit means the same blank-unit entry can silently resolve differently
  depending on factors no one configured on purpose.
DISCONFIRMING_OBSERVATION: >
  Two otherwise-identical records with no unit explicitly specified resolve to different default
  units, or the resolved default cannot be traced back to any documented configuration setting.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create two otherwise-identical records with no unit specified and compare the resolved default
  unit and its configuration source for each.
```
## G03-UOM-Q031

```yaml
QID: G03-UOM-Q031
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  When both a category-level default rounding/precision setting and a record-level override
  exist and disagree, one documented rule decides which applies, and that rule is honoured
  consistently by every consuming process.
WHY_IT_MATTERS: >
  Without one documented precedence, different parts of the system can each "correctly" apply a
  different one of the two settings, and no single figure is provably right.
DISCONFIRMING_OBSERVATION: >
  Two different consuming processes, reading the same record with a category default and a
  record-level override that disagree, apply different settings from each other.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  A record with a rounding/precision override that differs from its category's default; check
  which setting two independent consuming processes apply.
```

## G03-UOM-Q032

```yaml
QID: G03-UOM-Q032
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A quantity valued for accounting or costing purposes and the same quantity displayed in an
  operational, non-accounting context are computed from the same underlying conversion, not two
  independently rounded results that can diverge from each other.
WHY_IT_MATTERS: >
  A silent divergence between the operational and financial view of the same quantity means
  operations and finance can each be confidently looking at a different truth.
DISCONFIRMING_OBSERVATION: >
  The same transaction's quantity, read from an operational (non-accounting) view and from its
  accounting/costing record, disagrees by more than the documented rounding tolerance.
EXPECTED_SURFACE: S1,S2,S5
PRECONDITIONS: >
  A transaction with a non-trivial conversion applied; compare its quantity as shown in an
  operational view against its quantity as recorded for accounting/costing.
```

## G03-UOM-Q033

```yaml
QID: G03-UOM-Q033
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where a tax rule is computed from a quantity or a quantity-derived value, the quantity used for
  the tax calculation is the same converted quantity used for the rest of the transaction, not a
  separately re-derived figure that can disagree with it.
WHY_IT_MATTERS: >
  A tax calculation silently using a different converted quantity than the transaction itself
  creates a tax figure that cannot be reconciled back to the transaction it is supposed to tax.
DISCONFIRMING_OBSERVATION: >
  The quantity used in a tax computation for a transaction differs from the quantity recorded on
  that same transaction after conversion, with no documented reason for a separate basis.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A transaction whose tax is computed from a quantity that has passed through unit conversion;
  compare the quantity basis used for tax against the transaction's own recorded quantity.
```

## G03-UOM-Q034

```yaml
QID: G03-UOM-Q034
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling or reversing a transaction that used a non-reference unit produces an exact inverse
  effect on quantity and valuation, within tolerance, rather than a partial or asymmetric
  reversal.
WHY_IT_MATTERS: >
  An asymmetric reversal leaves a residual quantity or value on the books that a routine
  cancellation should have fully cleared.
DISCONFIRMING_OBSERVATION: >
  Cancelling or reversing a transaction posted in a non-reference unit leaves a net non-zero
  quantity or valuation impact greater than the documented rounding tolerance.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Post a transaction in a non-reference unit, cancel or reverse it, and check the net quantity
  and valuation impact.
```

## G03-UOM-Q035

```yaml
QID: G03-UOM-Q035
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A user without configuration-level authorization cannot alter a unit's conversion factor or
  category assignment through any available path, including one not gated by the primary
  configuration screen.
WHY_IT_MATTERS: >
  A second, ungated path to change a conversion factor turns a governed, auditable change into
  an unreviewed one that bypasses whatever control the primary screen enforces.
DISCONFIRMING_OBSERVATION: >
  A user lacking configuration-level authorization succeeds in changing a unit's conversion
  factor or category assignment through a path other than the primary, permission-gated
  configuration screen.
EXPECTED_SURFACE: S3,S4,S7
PRECONDITIONS: >
  A user account without configuration authorization; attempt to alter a conversion factor or
  category assignment through every available supported path, not only the primary screen.
```

## G03-UOM-Q036

```yaml
QID: G03-UOM-Q036
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Where multi-unit functionality is configurable as optional, turning it off after multi-unit
  data already exists does not silently discard or misinterpret the existing multi-unit history.
WHY_IT_MATTERS: >
  Toggling a convenience setting off should never be able to destroy or corrupt data that was
  captured while the setting was on.
DISCONFIRMING_OBSERVATION: >
  Disabling multi-unit functionality after transactions with a non-reference unit already exist
  causes those transactions to display, value, or report a different quantity than before the
  setting was disabled.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Create transactions using a non-reference unit while multi-unit functionality is enabled, then
  disable it and re-check those transactions.
```

## G03-UOM-Q037

```yaml
QID: G03-UOM-Q037
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Converting a quantity through an intermediate unit (first unit to a second, then the second to
  a third) yields the same result, within tolerance, as converting directly from the first unit
  to the third, when both paths are defined for the same category.
WHY_IT_MATTERS: >
  A workflow that happens to route a quantity through an extra unit should never itself change
  the answer — if it does, the conversion logic is path-dependent rather than mathematically
  sound.
DISCONFIRMING_OBSERVATION: >
  Converting a fixed quantity through an intermediate unit produces a result that differs, by
  more than the documented tolerance, from converting the same quantity directly between the
  first and third units.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A category with three units where both a chained and a direct conversion path exist between
  the first and third; compare both paths for the same source quantity.
```

## G03-UOM-Q038

```yaml
QID: G03-UOM-Q038
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Renaming a unit's display label does not change its identity for the purpose of matching
  historical records, conversions already stored, or integration references that used the
  earlier label.
WHY_IT_MATTERS: >
  If identity is tied to a display label rather than a stable underlying reference, a purely
  cosmetic rename can silently orphan every historical record and integration mapping that used
  the old label.
DISCONFIRMING_OBSERVATION: >
  After a unit's display label is changed, a historical transaction, a stored conversion, or an
  integration reference that used the original label fails to resolve, or resolves to a
  different unit.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  A unit referenced by a historical transaction and by an integration mapping; rename its
  display label and re-check both references.
```

## G03-UOM-Q039

```yaml
QID: G03-UOM-Q039
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When inventory is valued in a costing or valuation unit different from the transactional unit,
  the conversion applied at valuation time is the same conversion that would be reconstructed
  from the transaction's own recorded factor, not a separately maintained value that can drift
  from it.
WHY_IT_MATTERS: >
  Two independently maintained conversions for the same physical movement — one for the
  transaction, one for valuation — will eventually disagree, and the disagreement lands directly
  in the financial statements.
DISCONFIRMING_OBSERVATION: >
  The conversion factor implied by a valuation-layer figure for a transaction differs from the
  conversion factor recorded on that transaction itself, for the same unit pair and the same
  point in time.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  A transaction whose transactional unit differs from its stock valuation unit; independently
  derive the conversion factor from each side and compare.
```

## G03-UOM-Q040

```yaml
QID: G03-UOM-Q040
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A scheduled or background pass that recalculates quantities or valuations, such as a periodic
  reconciliation, uses the historically-correct conversion factor for each transaction's own
  original date, not the factor currently active at the time the background pass runs.
WHY_IT_MATTERS: >
  A background job that applies today's factor to yesterday's transactions silently rewrites
  history every time it runs, in a way that is easy to mistake for a legitimate reconciliation
  finding.
DISCONFIRMING_OBSERVATION: >
  A scheduled recalculation pass, run after a conversion factor has changed, alters the recorded
  value of a transaction that was posted before the factor change, using the new factor instead
  of the factor in force at posting.
EXPECTED_SURFACE: S1,S2,S6,S8
PRECONDITIONS: >
  Post a transaction under one factor, change the factor, then run the scheduled/background
  recalculation and check whether the original transaction's value changed.
```
## G03-UOM-Q041

```yaml
QID: G03-UOM-Q041
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Converting a quantity down to a coarser unit and then re-splitting it back into the original
  finer unit does not create or destroy quantity beyond the tolerance defined for a single
  conversion step.
WHY_IT_MATTERS: >
  A downgrade-then-split cycle that leaks or fabricates quantity is a quiet way for stock counts
  to drift purely from routine unit conversions, with no transaction obviously at fault.
DISCONFIRMING_OBSERVATION: >
  Converting a known quantity to a coarser unit and then splitting it back into the original
  finer unit yields a total that differs from the original by more than the single-conversion
  tolerance.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A quantity in a fine unit; convert to a coarser unit of the same category and then re-split
  back to the original unit, comparing totals.
```

## G03-UOM-Q042

```yaml
QID: G03-UOM-Q042
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Converting a quantity through two sequential unit conversions within one transaction produces
  the same tolerance-bounded result as a single direct conversion between the same starting and
  ending units — the number of conversion hops in a workflow does not itself change the outcome.
WHY_IT_MATTERS: >
  If the number of hops changes the answer, two business processes that reach the same unit pair
  by different routes will silently disagree with each other.
DISCONFIRMING_OBSERVATION: >
  A quantity converted through two sequential hops within a single transaction differs, by more
  than the documented tolerance, from the same quantity converted directly between the same
  starting and ending units in a single step.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Construct one workflow that reaches a target unit through two sequential conversions and
  another that reaches it directly, from the same starting quantity, and compare results.
```

## G03-UOM-Q043

```yaml
QID: G03-UOM-Q043
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When a user manually overrides a system-computed converted quantity on a document line, the
  override is recorded as distinct from the originally computed value, and downstream processes
  are told explicitly which of the two figures is authoritative.
WHY_IT_MATTERS: >
  If a manual override is indistinguishable from a system computation, no one can later tell
  whether an unusual quantity reflects a real business decision or a conversion defect.
DISCONFIRMING_OBSERVATION: >
  After a manual override of a computed converted quantity, the original system-computed value
  is no longer retrievable, or a downstream process silently reverts to the original computed
  value without indicating that an override existed.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  A document line with a system-computed converted quantity; manually override it and trace
  which value downstream processes and audit history subsequently show.
```

## G03-UOM-Q044

```yaml
QID: G03-UOM-Q044
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A unit or category configured as private to one company does not appear as selectable, and its
  factor is not silently applied, on a document belonging to a different company.
WHY_IT_MATTERS: >
  A private unit leaking across a company boundary means one business's internal unit
  arrangement can silently affect a completely unrelated company's transactions.
DISCONFIRMING_OBSERVATION: >
  A unit or category configured as private to one company either appears as selectable, or its
  conversion factor is applied, on a document belonging to a different company.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  A unit or category marked private to one company; attempt to select it, or trigger a
  conversion using it, from a document belonging to a different company.
```

## G03-UOM-Q045

```yaml
QID: G03-UOM-Q045
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A unit that has never been referenced by any transaction can be permanently removed, while a
  unit that has ever been referenced by a transaction is prevented from permanent removal and
  only archival is offered — the system does not allow the two outcomes to be interchanged.
WHY_IT_MATTERS: >
  Permanently removing a unit that has transaction history destroys the ability to ever read
  that history again, and should never be reachable by the same action as removing an unused
  one.
DISCONFIRMING_OBSERVATION: >
  A unit that has been referenced by at least one transaction is permanently removable through
  some available path, rather than being restricted to archival only.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  One unit never referenced by a transaction and one unit with at least one transaction; attempt
  permanent removal on each through every available supported path.
```

## G03-UOM-Q046

```yaml
QID: G03-UOM-Q046
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Two tenants that each define a category or unit with the same display name or code do not
  share, merge, or cross-reference each other's conversion factors as a result of that name
  collision.
WHY_IT_MATTERS: >
  A name-based collision across tenants would mean one customer's conversion configuration can
  silently determine another, unrelated customer's converted quantities.
DISCONFIRMING_OBSERVATION: >
  Two tenants defining a unit or category with an identical display name or code end up sharing
  a single conversion factor, or a change under one tenant's definition affects the other
  tenant's stored data.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Two tenants each define a unit or category using the same display name/code with different
  conversion factors; check whether either tenant's data is affected by the other's definition.
```

## G03-UOM-Q047

```yaml
QID: G03-UOM-Q047
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A change to a currency or a price does not, by itself, alter a stored unit conversion factor —
  quantity conversion and monetary valuation are computed independently even when they appear
  together in a single converted line amount.
WHY_IT_MATTERS: >
  If currency or price changes can leak into the quantity conversion, a purely monetary event
  would silently corrupt physical quantity records, which is a much harder defect to trace back.
DISCONFIRMING_OBSERVATION: >
  Changing a currency or a price on a document line changes the unit conversion factor applied
  to that line's quantity, or changes the converted quantity itself, independent of any quantity
  or unit change.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A document line with a defined unit conversion; change only its currency or price and check
  whether the converted quantity or the conversion factor changes.
```

## G03-UOM-Q048

```yaml
QID: G03-UOM-Q048
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A transaction entered with a posting date earlier than the most recent conversion-factor
  change applies the factor that was in force on that earlier posting date, not the factor
  currently active at the time of data entry.
WHY_IT_MATTERS: >
  A backdated transaction that silently applies today's factor instead of the factor that was
  actually in force on its stated date makes the posting date itself unreliable evidence of what
  happened.
DISCONFIRMING_OBSERVATION: >
  A transaction backdated to before a conversion-factor change is applied using the current
  (post-change) factor rather than the factor that was in force on the transaction's stated
  posting date.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Change a conversion factor, then enter a transaction with a posting date earlier than the
  change, and check which factor was actually applied.
```

## G03-UOM-Q049

```yaml
QID: G03-UOM-Q049
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A category configured with only one unit, requiring no conversion, is handled by the same
  general conversion logic as a multi-unit category collapsed to a one-to-one factor, rather than
  a special-cased shortcut that behaves differently once a second unit is later added.
WHY_IT_MATTERS: >
  A special-cased single-unit shortcut that bypasses the general conversion path can leave latent
  defects undiscovered until the day a second unit is added and the category suddenly needs the
  general path it never actually exercised.
DISCONFIRMING_OBSERVATION: >
  Adding a second unit to a previously single-unit category changes the stored or displayed
  quantity of an existing transaction that used the original, sole unit, with no conversion event
  explicitly recorded.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  A category with exactly one unit and existing transactions; add a second unit to the category
  and re-check the existing transactions' stored and displayed quantity.
```

## G03-UOM-Q050

```yaml
QID: G03-UOM-Q050
MODULE: uom
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Where a category's conversion factor between two units can be reached both through the
  category's own factor definition and independently derived from each unit's individually
  stored factor relative to the reference unit, both routes agree for every unit pair, rather
  than producing two disagreeing answers for the same conversion.
WHY_IT_MATTERS: >
  Two independently stored sources for the same conversion fact will eventually be edited out of
  step with each other, and whichever one a given process happens to read determines a silently
  wrong answer.
DISCONFIRMING_OBSERVATION: >
  The conversion factor between two units, computed via each unit's individually stored factor
  relative to the reference unit, disagrees with the conversion factor obtained directly for that
  pair, for the same category at the same point in time.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  A category where a unit pair's conversion can be derived two ways (via each unit's own factor
  to the reference unit, and via any directly defined pairwise factor); compute both and compare.
```
