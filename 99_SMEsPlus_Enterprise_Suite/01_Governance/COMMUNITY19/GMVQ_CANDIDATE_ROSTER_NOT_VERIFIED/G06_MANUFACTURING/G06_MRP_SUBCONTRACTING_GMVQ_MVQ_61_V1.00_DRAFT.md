# SMEsPlus ENTERPRISE SUITE
## GMVQ — G06 MANUFACTURING / mrp_subcontracting Module Adversarial MVQ Bank (Family Base)

**Document ID:** GMVQ-G06-MRP_SUBCONTRACTING-MVQ61-V1.00
**Group:** G06 MANUFACTURING
**Module Metadata:** `mrp_subcontracting`
**Wave:** W2
**Author Cell:** GMVQ PRODUCTION TEAM P11 (GMVQ Question Factory — Wave W2 Production Cell P11)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 61

## Purpose

`mrp_subcontracting` is the FAMILY BASE for a six-variant group of modules that all describe one defining
condition: production happens somewhere the operator cannot see, on stock the operator still owns, performed by
a party the operator does not control. This bank owns that condition's own invariants directly, so that the five
sibling variant banks (`mrp_subcontracting_account`, `_purchase`, `_dropshipping`, `_landed_costs`, `_repair`) do
not each have to restate them and do not collapse into five copies of one bank with a noun swapped. Per the GMVQ
Bridge Module Rule, this bank asks what is true of the underlying arrangement itself; each sibling bank asks only
what breaks at the seam when its own second capability is attached to that arrangement.

Question text is source-neutral: no vendor or product name, no technical identifier (model, table, field, method,
XML ID, API path), and no reference to how any specific implementation is built. The module's own metadata name
is confined to the `MODULE:` field. Language throughout is generic business/behavioural language — "an outside
party", "the arrangement", "the order" — never the module's own technical name.

## Control

- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong.
- No padding: 61 questions exist because they test 61 distinct material hypotheses, spread across business
  capability, business rule, state transition, configuration dependency, role/permission, exception path,
  cancellation, reversal, negative case, company/branch boundary, auditability, concurrency/ordering, and
  runtime/configuration reachability. No two questions share the same disconfirming event.
- `LAYER: BASE` marks a foundation/configuration-time question (arrangement setup, bill-of-materials dependency,
  location and party setup, permission definition); `LAYER: PROCESS` marks a transactional, in-flight question
  (send, partial return, receipt, cancellation, period close), since this module carries both layers.
- **Exclusion list — deliberately left to the sibling banks in this family, per the Bridge Module Rule and the
  G06 Group Brief.** None of the following is asked here; each is recorded against the bank that owns it so the
  five variant cells do not need to rediscover this boundary themselves:
  - the ledger and valuation consequence of stock owned by the sender while it sits at an outside party ->
    `mrp_subcontracting_account`
  - the commercial document that pays for the arrangement, and its disagreement with the production side on
    quantity, price, receipt date, and who confirms what first -> `mrp_subcontracting_purchase`
  - output that is shipped directly onward and never physically received back by the sender at all, and the
    resulting double absence of physical custody -> `mrp_subcontracting_dropshipping`
  - a cost that arrives after output the sender never physically held has already been consumed or moved on ->
    `mrp_subcontracting_landed_costs`
  - an item's identity and warranty status as it passes through an external repair loop ->
    `mrp_subcontracting_repair`
  - As of this draft, no sibling bank yet exists on disk for this group (G06 MANUFACTURING is unauthored). This
    exclusion list is recorded here specifically so the five sibling cells can author against it without
    restating this bank's ground or duplicating each other.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `module + QID` is a Research
  Evidence Join Key only; no Formal Coverage is derived from this bank.
- Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G06-MRP_SUBCONTRACTING-Q001

```yaml
QID: G06-MRP_SUBCONTRACTING-Q001
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Components physically located at an outside party remain in the sending organisation's own stock ownership
  records until a receipt of finished output, or another defined closing event, reassigns them — they are not
  removed from the sender's inventory the moment they physically leave the sender's premises.
WHY_IT_MATTERS: >
  If ownership drops at the moment of physical departure, the sender's stock valuation and physical-count
  reconciliation permanently understate assets it still owns and remains liable for if they are lost.
DISCONFIRMING_OBSERVATION: >
  Sending components out to an outside party removes them entirely from every stock ownership record, with
  nothing left indicating the sender still owns that quantity.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create an order for production to be performed by an outside party, send a tracked component quantity to that
  party, and inspect whether any stock record still attributes ownership of that quantity to the sender.
```

## G06-MRP_SUBCONTRACTING-Q002

```yaml
QID: G06-MRP_SUBCONTRACTING-Q002
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  For any quantity currently away from the sender's own premises, the system distinguishes quantity held at an
  outside party from quantity at the sender's other own sites, rather than reporting all off-premises quantity
  identically.
WHY_IT_MATTERS: >
  Physical counts, insurance discussions, and liability questions require knowing specifically what sits at a
  third party's premises, not merely that it is "not here."
DISCONFIRMING_OBSERVATION: >
  A stock position report cannot distinguish quantity held at an outside party from quantity held at another of
  the sender's own sites.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Hold stock at both an outside party and at an internal secondary site simultaneously, then produce a position
  report and check whether the two categories can be told apart.
```

## G06-MRP_SUBCONTRACTING-Q003

```yaml
QID: G06-MRP_SUBCONTRACTING-Q003
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A location record used to represent stock held at an outside party carries an association with a specific
  external party identity, so stock cannot sit "at an outside party" in the abstract with no accountable party
  attached.
WHY_IT_MATTERS: >
  Without an accountable party attached, there is no one to hold responsible for loss and no one to contact or
  claim against.
DISCONFIRMING_OBSERVATION: >
  A location representing off-site custody can exist and hold quantity with no external party identifiable from
  it.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Inspect how an off-site custody location is configured and attempt to create or use one with no external party
  identity attached.
```

## G06-MRP_SUBCONTRACTING-Q004

```yaml
QID: G06-MRP_SUBCONTRACTING-Q004
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Stock recorded as held at an outside party is excluded from counts and valuations scoped to the sender's own
  physical premises, so a warehouse-level physical count at that premises is not expected to find it there.
WHY_IT_MATTERS: >
  Staff who are not told to exclude off-site custody will report false shrinkage for stock that was never
  physically missing, only situated elsewhere.
DISCONFIRMING_OBSERVATION: >
  A physical count scoped to one premises is reconciled against a total that silently includes quantity known to
  be located elsewhere.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Run a physical count scoped to a single premises while some owned quantity sits at an outside party and check
  what total the count is reconciled against.
```

## G06-MRP_SUBCONTRACTING-Q005

```yaml
QID: G06-MRP_SUBCONTRACTING-Q005
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  The record of stock held at an outside party captures physical and quantity custody only; it does not itself
  assert or derive who bears financial loss if the stock is damaged or lost there, leaving that question to
  whatever separate contractual record exists.
WHY_IT_MATTERS: >
  If the system silently implies a risk allocation it never actually established, staff could rely on it as
  though it were legally decided.
DISCONFIRMING_OBSERVATION: >
  The system presents a definitive statement of financial liability for loss at an outside party's premises as an
  established fact, with no reference to a separate contractual source.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Review any screen or report describing stock held at an outside party and check whether it makes a liability
  claim beyond quantity and location.
```

## G06-MRP_SUBCONTRACTING-Q006

```yaml
QID: G06-MRP_SUBCONTRACTING-Q006
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Components sent to an outside party that are never returned, and never appear on any incoming receipt, remain
  visible indefinitely as an open outstanding quantity rather than being silently dropped from every record after
  a period of inactivity.
WHY_IT_MATTERS: >
  Silent disappearance of an unresolved send prevents anyone from ever discovering, investigating, or recovering
  value for components that were never accounted for.
DISCONFIRMING_OBSERVATION: >
  A component quantity sent out and never returned stops appearing anywhere as outstanding once enough time or
  activity has passed, with no closing event ever recorded against it.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Send components to an outside party, record no return or consumption against them, and check the outstanding
  balance after a long period and after unrelated activity has occurred.
```

## G06-MRP_SUBCONTRACTING-Q007

```yaml
QID: G06-MRP_SUBCONTRACTING-Q007
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a finished-output receipt implies a smaller component consumption than what was actually sent, the
  difference remains visible as an unresolved outstanding balance rather than being automatically written off as
  consumed.
WHY_IT_MATTERS: >
  Automatic write-off would hide shortage, theft, or an outside party's error inside a number that looks like
  ordinary completed consumption.
DISCONFIRMING_OBSERVATION: >
  Receiving fewer finished units than the bill of materials would justify for the quantity sent silently closes
  out the full sent quantity as consumed, leaving no visible outstanding balance.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a known component quantity, receive back fewer finished units than the bill of materials would support,
  and check what outstanding balance remains.
```

## G06-MRP_SUBCONTRACTING-Q008

```yaml
QID: G06-MRP_SUBCONTRACTING-Q008
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A finished-output receipt can be recorded even when the receiving user notes that the physical item received
  does not match the item the order specifies, and that mismatch is captured rather than silently coerced into
  the ordered item's identity.
WHY_IT_MATTERS: >
  Silently recording the ordered item regardless of what physically arrived would corrupt the sender's own
  inventory identity and could disguise a substitution or an outside party's error.
DISCONFIRMING_OBSERVATION: >
  There is no way to record that what arrived differs in identity from what the order specified; the receipt can
  only be filed under the ordered item's identity regardless of what was physically checked in.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Attempt to record a finished-output receipt where the physical item checked in differs from the ordered item
  and observe whether that difference can be captured.
```

## G06-MRP_SUBCONTRACTING-Q009

```yaml
QID: G06-MRP_SUBCONTRACTING-Q009
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A component quantity recorded as sent to a given outside party for a given order cannot be reported by that
  same party as consumed against a different order without an explicit reallocation event visible in both
  orders' records.
WHY_IT_MATTERS: >
  Without a visible reallocation, one order's paid-for materials could be quietly used to fulfil a different
  order, and neither order's records would show what actually happened.
DISCONFIRMING_OBSERVATION: >
  Consumption reported against one order can be satisfied using a component balance sent under a different
  order's own send record, with no reallocation event recorded anywhere.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send components under two separate orders to the same outside party, then attempt to record consumption for
  one order against the balance sent under the other.
```

## G06-MRP_SUBCONTRACTING-Q010

```yaml
QID: G06-MRP_SUBCONTRACTING-Q010
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Where component ownership at an outside party is tracked as a pooled balance rather than tied to one order,
  that pooled balance is still traceable back to the individual send events that built it up, rather than
  existing only as an unexplained running total.
WHY_IT_MATTERS: >
  An unexplained pooled total cannot be reconciled to what was actually sent over time, making shortfall or
  diversion undetectable.
DISCONFIRMING_OBSERVATION: >
  A pooled outstanding balance at an outside party can be inspected with no way to trace it back to the
  individual send transactions that contributed to it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Build up a pooled outstanding balance at one outside party from several separate sends and attempt to trace the
  total back to each contributing event.
```

## G06-MRP_SUBCONTRACTING-Q011

```yaml
QID: G06-MRP_SUBCONTRACTING-Q011
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Recording that components at an outside party were lost, damaged, or will never be returned is a distinct,
  visible event from an ordinary return, and does not require inventing a fictitious return to close the
  outstanding balance.
WHY_IT_MATTERS: >
  If the only way to close a balance is to pretend the components came back, the record permanently misstates
  what actually happened to them.
DISCONFIRMING_OBSERVATION: >
  The only way to remove an outstanding component balance at an outside party is to record a return; there is no
  separate way to record and close a loss.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Attempt to close an outstanding component balance by recording a genuine loss rather than a return and check
  whether a distinct event type is available.
```

## G06-MRP_SUBCONTRACTING-Q012

```yaml
QID: G06-MRP_SUBCONTRACTING-Q012
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Recording receipt of finished output from an outside party requires, or automatically produces, a
  corresponding record of the component quantities considered consumed for that receipt, rather than allowing a
  finished-output receipt with no linked consumption record at all.
WHY_IT_MATTERS: >
  A finished-output receipt with no consumption record makes it impossible to know what happened to the
  components sent, hiding shortage or diversion behind an apparently normal completion.
DISCONFIRMING_OBSERVATION: >
  A finished-output receipt from an outside party can be completed and posted to stock with no component
  consumption record linked to it at all.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a finished-output receipt from an outside party and check whether any component consumption record is
  created or required alongside it.
```

## G06-MRP_SUBCONTRACTING-Q013

```yaml
QID: G06-MRP_SUBCONTRACTING-Q013
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  The component consumption linked to a finished-output receipt is presented as a derived, calculated figure
  based on the bill of materials rather than as an independently observed fact, and the record does not claim a
  certainty the organisation never actually had.
WHY_IT_MATTERS: >
  Presenting a calculated figure as an observed fact would overstate confidence in a number that could be wrong
  if the outside party actually used different quantities.
DISCONFIRMING_OBSERVATION: >
  The consumption figure attached to a finished-output receipt is labelled or treated identically to a directly
  observed count, with nothing distinguishing it as a derived expectation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Inspect how a consumption figure is presented on a finished-output receipt and check for any labelling
  distinguishing calculation from observation.
```

## G06-MRP_SUBCONTRACTING-Q014

```yaml
QID: G06-MRP_SUBCONTRACTING-Q014
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Receiving a finished-output quantity larger than the components on record as sent could support under the bill
  of materials is flagged as an exception requiring attention, rather than accepted silently.
WHY_IT_MATTERS: >
  Excess output relative to what was sent is either an error or evidence the outside party drew on its own or
  another party's material, and both need investigation.
DISCONFIRMING_OBSERVATION: >
  A finished-output quantity that mathematically could not have been produced from the components on record as
  sent is accepted into stock with no exception raised.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a finished-output receipt whose quantity exceeds what the sent components and the bill of materials
  could support, and check whether any exception is raised.
```

## G06-MRP_SUBCONTRACTING-Q015

```yaml
QID: G06-MRP_SUBCONTRACTING-Q015
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Confirming a finished-output receipt does not itself retroactively alter the record of what components were
  originally sent; the send record and the receipt record remain two independent, separately dated facts.
WHY_IT_MATTERS: >
  If confirming a receipt can rewrite the send history, the audit trail loses its ability to show what was
  actually sent versus what was later inferred.
DISCONFIRMING_OBSERVATION: >
  Confirming a finished-output receipt changes the quantity or date shown on the original component send record
  rather than leaving it as originally recorded.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a component send, then confirm a finished-output receipt against it, and check whether the original send
  record's quantity or date has changed.
```

## G06-MRP_SUBCONTRACTING-Q016

```yaml
QID: G06-MRP_SUBCONTRACTING-Q016
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Two orders for the same finished item, produced under two different arrangements — one where the sender
  supplies all components and one where the outside party sources some components itself — expect different
  component consumption records, rather than the system forcing a single consumption pattern regardless of which
  arrangement applies.
WHY_IT_MATTERS: >
  Treating both arrangements identically would either overstate what the sender is owed back or falsely record
  consumption of components the sender never actually sent.
DISCONFIRMING_OBSERVATION: >
  An order under an arrangement where the outside party sources its own components still generates an expected
  consumption record identical to one where the sender supplies everything.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure one arrangement where the sender supplies everything and one where the outside party sources some
  components itself, then compare the expected consumption records each produces.
```

## G06-MRP_SUBCONTRACTING-Q017

```yaml
QID: G06-MRP_SUBCONTRACTING-Q017
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Changing the bill of materials for an item produced by an outside party, after components have already been
  sent under the previous version, does not retroactively rewrite what was actually sent under the earlier
  version.
WHY_IT_MATTERS: >
  Retroactive rewriting would make it impossible to know what quantity of components a party actually received at
  the time it received them.
DISCONFIRMING_OBSERVATION: >
  Revising the bill of materials changes the recorded quantity of a component already sent under an order created
  before the revision.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send components under one version of a bill of materials, revise the bill of materials, and check whether the
  historical send record changed.
```

## G06-MRP_SUBCONTRACTING-Q018

```yaml
QID: G06-MRP_SUBCONTRACTING-Q018
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  When no bill of materials exists, or none is configured for a finished item produced by an outside party, the
  system prevents or clearly flags an order that has no basis for calculating what components should be sent.
WHY_IT_MATTERS: >
  Sending or expecting components with no defined bill of materials removes the only reference point for judging
  over- or under-consumption later.
DISCONFIRMING_OBSERVATION: >
  An order can proceed to sending components and receiving finished output while its item has no bill of
  materials defined, with no flag raised.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to create and progress an order for an item with no bill of materials configured and check whether it
  is blocked or flagged.
```

## G06-MRP_SUBCONTRACTING-Q019

```yaml
QID: G06-MRP_SUBCONTRACTING-Q019
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A component listed on the bill of materials as optional, or as a substitute alternative, is reflected in the
  expected consumption record according to which actual alternative was used, rather than the system always
  assuming the first-listed option.
WHY_IT_MATTERS: >
  Assuming the wrong alternative silently misstates which specific component quantity the sender should expect to
  reconcile against the outside party.
DISCONFIRMING_OBSERVATION: >
  Sending a substitute alternative component still generates an expected consumption record naming the original,
  unsent alternative.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a bill of materials with an alternative component, send the substitute alternative rather than the
  default, and check which component the expected consumption record names.
```

## G06-MRP_SUBCONTRACTING-Q020

```yaml
QID: G06-MRP_SUBCONTRACTING-Q020
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  An arrangement can define that certain components are supplied directly by the outside party itself rather than
  sent by the sender, and such components are excluded from what the sender expects to reconcile as
  sent-and-consumed.
WHY_IT_MATTERS: >
  Expecting reconciliation of components the sender never owned or sent would create a permanent, unresolvable
  discrepancy with no actual error behind it.
DISCONFIRMING_OBSERVATION: >
  A component the arrangement defines as outside-party-supplied still appears on the sender's own
  outstanding-balance or reconciliation record as if the sender had sent it.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a component as supplied by the outside party rather than the sender, and check whether it appears on
  the sender's own outstanding-balance record.
```

## G06-MRP_SUBCONTRACTING-Q021

```yaml
QID: G06-MRP_SUBCONTRACTING-Q021
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Yield loss occurring during an operation performed at an outside party — components consumed that appear in
  neither finished nor scrap output — can be recorded as a distinct outcome from either successful output or a
  formally returned scrap item.
WHY_IT_MATTERS: >
  Without a way to record invisible yield loss, the only options are to falsely show full output or to leave the
  missing quantity as an unexplained permanent discrepancy.
DISCONFIRMING_OBSERVATION: >
  The system provides no way to record component quantity consumed at an outside party that resulted in neither
  finished output nor a returned scrap item.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Attempt to record a quantity of components consumed at an outside party that produced neither finished output
  nor scrap and check whether a distinct record exists for it.
```

## G06-MRP_SUBCONTRACTING-Q022

```yaml
QID: G06-MRP_SUBCONTRACTING-Q022
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Scrap generated during an operation at an outside party is attributable to the specific order and outside party
  involved, rather than a general scrap rate being distributable across unrelated orders.
WHY_IT_MATTERS: >
  Spreading scrap across unrelated orders hides which specific arrangement or outside party is actually
  generating loss, defeating any attempt to hold a party accountable.
DISCONFIRMING_OBSERVATION: >
  Scrap quantity recorded during production at an outside party cannot be traced back to the specific order or
  outside party where it occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record scrap generated during outside-party production and check whether it can be traced back to the specific
  order and party involved.
```

## G06-MRP_SUBCONTRACTING-Q023

```yaml
QID: G06-MRP_SUBCONTRACTING-Q023
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  The bill of materials can define an accepted yield-loss allowance for an operation performed at an outside
  party, and consumption within that allowance is treated differently from consumption that exceeds it.
WHY_IT_MATTERS: >
  Treating expected, contractually tolerated loss the same as an anomalous overage removes the ability to flag
  the overage as something worth investigating.
DISCONFIRMING_OBSERVATION: >
  A yield loss far in excess of any defined allowance raises no different signal than a yield loss within the
  allowance.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a yield-loss allowance, then record a loss within it and a loss well beyond it, and compare what
  signal each produces.
```

## G06-MRP_SUBCONTRACTING-Q024

```yaml
QID: G06-MRP_SUBCONTRACTING-Q024
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether scrap or yield loss at an outside party is charged back to the sender, absorbed by the outside party, or
  shared, is a fact the arrangement records rather than one the system assumes by default.
WHY_IT_MATTERS: >
  An assumed default that does not match the actual commercial arrangement could misstate who is responsible for
  lost value with nothing prompting a check of the real agreement.
DISCONFIRMING_OBSERVATION: >
  The system presents a specific party as responsible for scrap loss with no configured basis for that
  attribution, as though it were a fixed rule rather than an arrangement-specific fact.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record a scrap loss at an outside party with no chargeback arrangement configured and check whether the system
  nonetheless presents an attribution of responsibility.
```

## G06-MRP_SUBCONTRACTING-Q025

```yaml
QID: G06-MRP_SUBCONTRACTING-Q025
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A component sent to an outside party under lot or serial tracking retains its originating lot or serial identity
  in the sender's records for as long as it remains outstanding, rather than losing that identity the moment it
  leaves the sender's premises.
WHY_IT_MATTERS: >
  Losing lot or serial identity at the boundary defeats a recall or quality investigation that needs to trace
  exactly which units went where.
DISCONFIRMING_OBSERVATION: >
  Once sent to an outside party, a lot- or serial-tracked component quantity can no longer be identified by its
  originating lot or serial in any sender record.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a lot- or serial-tracked component to an outside party and check whether its lot or serial identity remains
  retrievable while outstanding.
```

## G06-MRP_SUBCONTRACTING-Q026

```yaml
QID: G06-MRP_SUBCONTRACTING-Q026
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When a received finished item is itself lot- or serial-tracked, the receipt record allows an association back to
  the component lots or serials sent for that order, to the extent the organisation has any way of knowing that
  association.
WHY_IT_MATTERS: >
  Without this association, a component-level quality problem discovered later cannot be traced forward to know
  which finished items might be affected.
DISCONFIRMING_OBSERVATION: >
  There is no way to associate a received finished item's lot or serial with the component lots or serials sent
  for the order that produced it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Receive a lot- or serial-tracked finished item from an order that sent lot- or serial-tracked components and
  check whether the two can be associated.
```

## G06-MRP_SUBCONTRACTING-Q027

```yaml
QID: G06-MRP_SUBCONTRACTING-Q027
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  If the outside party reports which specific component lot or serial it actually consumed, and that differs from
  what the sender's records show as sent under that lot, the discrepancy is capturable rather than one report
  silently overwriting the other.
WHY_IT_MATTERS: >
  Silently overwriting one side's record destroys the only evidence that the two parties' understanding of what
  was used ever differed.
DISCONFIRMING_OBSERVATION: >
  Entering the outside party's reported lot or serial consumption replaces the sender's original sent-lot record
  with no trace that the two disagreed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record an outside party's reported lot consumption that differs from the sender's own sent-lot record and check
  whether both versions remain visible.
```

## G06-MRP_SUBCONTRACTING-Q028

```yaml
QID: G06-MRP_SUBCONTRACTING-Q028
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Lot or serial tracking configured for a component does not stop being enforced once that component is sent to an
  outside party; a return or consumption record for it still requires the same lot or serial discipline as any
  other movement of it.
WHY_IT_MATTERS: >
  If tracking discipline relaxes at the boundary, the traceability chain has a gap exactly where the organisation
  has the least direct visibility.
DISCONFIRMING_OBSERVATION: >
  A component that requires lot or serial identification for every other movement can be recorded as returned or
  consumed from an outside party with no lot or serial identification required.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to record a return or consumption of a lot- or serial-tracked component from an outside party without
  providing a lot or serial and check whether it is accepted.
```

## G06-MRP_SUBCONTRACTING-Q029

```yaml
QID: G06-MRP_SUBCONTRACTING-Q029
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Recording a finished-output receipt does not require that the corresponding component send have already been
  recorded first; the system either prevents this ordering or clearly flags it, rather than silently accepting a
  receipt that logically precedes its own components' departure.
WHY_IT_MATTERS: >
  A receipt with no prior recorded send suggests either a data-entry backlog or components that left through some
  path the system never captured, and either case needs attention.
DISCONFIRMING_OBSERVATION: >
  A finished-output receipt is accepted and posted for an order with no component send ever recorded against it,
  with no exception or flag raised.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Attempt to record a finished-output receipt for an order that has no recorded component send and check whether
  it is blocked or flagged.
```

## G06-MRP_SUBCONTRACTING-Q030

```yaml
QID: G06-MRP_SUBCONTRACTING-Q030
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When a component send is recorded after its corresponding finished-output receipt has already been recorded,
  reflecting that the paperwork lagged the physical event, the system preserves both events' actual entered dates
  rather than silently reordering them to appear sequential.
WHY_IT_MATTERS: >
  Silently reordering dates to look sequential destroys the true timeline needed to investigate why the paperwork
  and the physical event diverged.
DISCONFIRMING_OBSERVATION: >
  Recording a late component send automatically changes its recorded date to fall before the already-recorded
  receipt, rather than keeping the dates as entered.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a finished-output receipt first, then record its component send afterward with its true late date, and
  check whether the entered dates are preserved.
```

## G06-MRP_SUBCONTRACTING-Q031

```yaml
QID: G06-MRP_SUBCONTRACTING-Q031
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  An outside party's own claimed production or completion date, where captured, is stored as a distinct fact from
  the date the sender's own system recorded the corresponding transaction, rather than the two dates being
  collapsed into one.
WHY_IT_MATTERS: >
  Collapsing the two dates removes the ability to detect and investigate a pattern where the outside party's
  actual timing habitually differs from what the paperwork shows.
DISCONFIRMING_OBSERVATION: >
  There is no way to record or distinguish an outside party's own claimed timing from the sender's own transaction
  recording date.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Attempt to capture an outside party's own claimed completion date separately from the sender's own recording
  date and check whether both can coexist.
```

## G06-MRP_SUBCONTRACTING-Q032

```yaml
QID: G06-MRP_SUBCONTRACTING-Q032
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling an order after components have already been sent does not automatically clear or hide the outstanding
  component balance at the outside party; the outstanding quantity remains visible and must be separately
  resolved.
WHY_IT_MATTERS: >
  Automatically clearing the balance on cancellation would make components physically still at a third party
  disappear from every record with no resolution.
DISCONFIRMING_OBSERVATION: >
  Cancelling an order removes all record of the component quantity still physically outstanding at the outside
  party.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send components under an order, cancel the order, and check whether the outstanding component balance at the
  outside party remains visible.
```

## G06-MRP_SUBCONTRACTING-Q033

```yaml
QID: G06-MRP_SUBCONTRACTING-Q033
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A cancelled order can still accept a subsequent return or receipt event addressing components that were already
  sent under it, rather than the cancelled status blocking any further recording against it.
WHY_IT_MATTERS: >
  If cancellation blocks all further recording, physically returned components have nowhere valid to be logged
  against, forcing a workaround that breaks the record's link to what actually happened.
DISCONFIRMING_OBSERVATION: >
  A cancelled order cannot accept any further return or receipt record, even though components sent under it are
  later physically returned.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Cancel an order with components already sent, then attempt to record a return of those components against the
  cancelled order.
```

## G06-MRP_SUBCONTRACTING-Q034

```yaml
QID: G06-MRP_SUBCONTRACTING-Q034
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling an order with components already partially consumed by the outside party requires a decision about
  the partially produced output and the consumed components, rather than the cancellation being treated as though
  no work had ever been performed.
WHY_IT_MATTERS: >
  Treating real, partially consumed components as though nothing happened would misstate the sender's stock
  position by the value of components that genuinely left and were used.
DISCONFIRMING_OBSERVATION: >
  Cancelling a partially consumed order returns the component quantities to standard on-hand stock as though they
  had never been sent or consumed at all.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send components, record partial consumption by the outside party, then cancel the order and check what happens
  to the consumed component quantities.
```

## G06-MRP_SUBCONTRACTING-Q035

```yaml
QID: G06-MRP_SUBCONTRACTING-Q035
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Who is permitted to cancel an order once components have already left the sender's premises is a distinct,
  at-least-as-restrictive permission from who may create the order in the first place.
WHY_IT_MATTERS: >
  A junior user able to cancel an order with real assets already committed to a third party could hide or obscure
  a problem that a more experienced reviewer would otherwise catch.
DISCONFIRMING_OBSERVATION: >
  Any user permitted to create an order can also cancel it after components have already been sent, with no
  additional permission checked.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Compare the permission required to create an order with the permission required to cancel it after components
  have been sent.
```

## G06-MRP_SUBCONTRACTING-Q036

```yaml
QID: G06-MRP_SUBCONTRACTING-Q036
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A single component send can be resolved through more than one partial return or consumption event over time,
  with the outstanding balance decreasing correctly after each one, rather than requiring the full original
  quantity to be resolved in a single event.
WHY_IT_MATTERS: >
  Real outside-party relationships return and consume material incrementally; forcing an all-or-nothing resolution
  would misstate the true outstanding position throughout the order's life.
DISCONFIRMING_OBSERVATION: >
  Recording a partial return against a component send does not reduce the outstanding balance correctly, or forces
  the remaining quantity to close out as if fully resolved.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a component quantity and record two separate partial returns against it over time, checking the outstanding
  balance after each.
```

## G06-MRP_SUBCONTRACTING-Q037

```yaml
QID: G06-MRP_SUBCONTRACTING-Q037
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When a component send has already been partially consumed and partially returned, a further finished-output
  receipt can still be recorded correctly against the remaining consumed portion, without requiring the earlier
  partial events to be undone or re-entered.
WHY_IT_MATTERS: >
  Requiring earlier events to be undone to record a later one would encourage staff to falsify history just to
  make the system accept a legitimate, ordinary event.
DISCONFIRMING_OBSERVATION: >
  Recording a finished-output receipt against a component send that already has a prior partial return requires
  deleting or altering that prior partial return first.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Record a partial return against a component send, then attempt to record a finished-output receipt for the
  remaining consumed portion without altering the partial return.
```

## G06-MRP_SUBCONTRACTING-Q038

```yaml
QID: G06-MRP_SUBCONTRACTING-Q038
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A partial return of components can be recorded as a different quantity from what a pre-calculated expectation
  would predict, with the discrepancy visible, rather than a partial return being forced to exactly match that
  expectation.
WHY_IT_MATTERS: >
  Forcing an exact match would make it impossible to record what an outside party actually, physically returned
  when it differs even slightly from expectation.
DISCONFIRMING_OBSERVATION: >
  The system rejects or silently adjusts a partial return quantity that does not exactly equal a pre-calculated
  expected figure, rather than recording what was actually returned.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt to record a partial return whose quantity differs from what a pre-calculated expectation would predict
  and check whether it is accepted as entered.
```

## G06-MRP_SUBCONTRACTING-Q039

```yaml
QID: G06-MRP_SUBCONTRACTING-Q039
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Multiple partial returns recorded against the same original send are each individually traceable to that
  original send, so the full history of how the original quantity was resolved can be reconstructed from separate
  events rather than only from a single final total.
WHY_IT_MATTERS: >
  Without individual traceability, an investigation into when and how much came back cannot distinguish one
  partial return from another.
DISCONFIRMING_OBSERVATION: >
  Only the cumulative total of all partial returns against a send is retained; the individual partial events
  cannot be separately identified or dated afterward.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record several partial returns against the same original send and check whether each is individually retrievable
  afterward.
```

## G06-MRP_SUBCONTRACTING-Q040

```yaml
QID: G06-MRP_SUBCONTRACTING-Q040
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  The system provides a way to record that an outside party relationship has ended, or can no longer be reached,
  while an outstanding component or expected-return balance still exists against it, rather than requiring that
  balance be artificially zeroed before the relationship record can be closed.
WHY_IT_MATTERS: >
  Forcing an artificial zero before closing the relationship would erase the very evidence needed to pursue
  recovery or write off the loss properly.
DISCONFIRMING_OBSERVATION: >
  An outside party relationship cannot be marked inactive or ended while it still carries an outstanding component
  balance; the balance must first be forced to zero with no separate record of why.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Attempt to deactivate or end an outside party relationship while an outstanding component balance still exists
  against it.
```

## G06-MRP_SUBCONTRACTING-Q041

```yaml
QID: G06-MRP_SUBCONTRACTING-Q041
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  An outstanding component or in-progress order balance associated with a specific outside party remains queryable
  and reportable as belonging to that party even after the party's own record is deactivated or archived.
WHY_IT_MATTERS: >
  If the historical balance becomes unreachable once the party is archived, no one can later produce evidence of
  what was owed when pursuing recovery or writing off the position.
DISCONFIRMING_OBSERVATION: >
  Deactivating or archiving an outside party's own record makes its historical outstanding component balance no
  longer retrievable.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Deactivate or archive an outside party with an outstanding component balance and check whether that balance is
  still retrievable.
```

## G06-MRP_SUBCONTRACTING-Q042

```yaml
QID: G06-MRP_SUBCONTRACTING-Q042
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Writing off a component balance that will never be recovered from an outside party is a distinct, identifiable
  event separate from an ordinary return, so a write-off does not read, after the fact, as though the components
  had been physically returned.
WHY_IT_MATTERS: >
  A write-off that looks like a return would misrepresent to anyone reviewing the record that the components
  actually came back, when in fact they were lost.
DISCONFIRMING_OBSERVATION: >
  The record of a written-off, unrecoverable component balance is indistinguishable after the fact from a record of
  an ordinary physical return.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Write off an unrecoverable component balance and compare the resulting record with an ordinary return record to
  see whether the two can be told apart.
```

## G06-MRP_SUBCONTRACTING-Q043

```yaml
QID: G06-MRP_SUBCONTRACTING-Q043
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  More than one open order or outstanding balance can exist against the same outside party at once, and each
  remains separately identifiable rather than being merged into a single combined figure.
WHY_IT_MATTERS: >
  A merged figure would make it impossible to tell which specific orders and components are at risk when a
  relationship with a given party breaks down.
DISCONFIRMING_OBSERVATION: >
  Multiple open orders against the same outside party can only be viewed as one combined outstanding figure, with
  no way to isolate which order contributes what.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Open two separate orders with outstanding balances against the same outside party and check whether each is
  separately reportable.
```

## G06-MRP_SUBCONTRACTING-Q044

```yaml
QID: G06-MRP_SUBCONTRACTING-Q044
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An accounting or reporting period can be closed while an in-progress order still has components outstanding at
  an outside party and no finished-output receipt recorded, without the period-close action itself forcing that
  order into a completed or resolved state it has not actually reached.
WHY_IT_MATTERS: >
  Forcing an unfinished order to appear resolved just to let a period close would misstate the true state of
  in-progress outside-party work at that period end.
DISCONFIRMING_OBSERVATION: >
  Closing a period automatically marks an in-progress order as completed or fully consumed even though no
  finished-output receipt has actually been recorded.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Close a reporting period while an order still has components outstanding at an outside party and check whether
  the order's status is altered by the close.
```

## G06-MRP_SUBCONTRACTING-Q045

```yaml
QID: G06-MRP_SUBCONTRACTING-Q045
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A report of components currently outstanding at outside parties can be produced as of a specific past date,
  reflecting what was actually outstanding at that date, rather than only what is outstanding as of today.
WHY_IT_MATTERS: >
  A period-end position that can only be viewed as of today cannot be reconstructed later for a prior close,
  undermining any review of an earlier period.
DISCONFIRMING_OBSERVATION: >
  The outstanding component position at outside parties can only be viewed for the current moment, with no way to
  reconstruct what it was as of an earlier period-end date.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Attempt to produce the outstanding-component position as of a past period-end date rather than the current date.
```

## G06-MRP_SUBCONTRACTING-Q046

```yaml
QID: G06-MRP_SUBCONTRACTING-Q046
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A component sent late in one period and returned or consumed early in the next period is attributed to the
  period in which each specific event actually occurred, rather than the entire quantity being attributed to a
  single period regardless of when each event happened.
WHY_IT_MATTERS: >
  Misattributing a straddling transaction to the wrong period misstates what was actually outstanding at each
  period's boundary.
DISCONFIRMING_OBSERVATION: >
  A component send and its later return that straddle a period boundary are both attributed to the same single
  period regardless of the date each individual event actually occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a component send just before a period boundary and its return just after, then check which period each
  event is attributed to.
```

## G06-MRP_SUBCONTRACTING-Q047

```yaml
QID: G06-MRP_SUBCONTRACTING-Q047
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An order that spans a period boundary while work is understood to be still in progress at the outside party does
  not require any component consumption or output to be estimated and force-recorded purely to make the
  period-end position appear reconciled.
WHY_IT_MATTERS: >
  Forcing an estimate purely to reconcile the period would introduce a fabricated number into a record whose value
  depends on reflecting only what actually happened.
DISCONFIRMING_OBSERVATION: >
  The period-close process requires entering an estimated consumption or output figure for a still-in-progress
  order before it will allow the period to close.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Attempt to close a period with a still-in-progress order outstanding and check whether an estimated figure is
  demanded before the close is allowed.
```

## G06-MRP_SUBCONTRACTING-Q048

```yaml
QID: G06-MRP_SUBCONTRACTING-Q048
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Confirming receipt of finished output from an outside party requires a distinct permission from the permission
  needed to create or send the original order, so the same single person is not necessarily both the one who
  committed the components and the one who alone attests to what came back.
WHY_IT_MATTERS: >
  If one person can unilaterally both send components and confirm what returned with no independent check, an
  error or a deliberate misstatement at either end has no second party positioned to notice it.
DISCONFIRMING_OBSERVATION: >
  The system defines no separate permission for confirming a finished-output receipt; any user able to create the
  order can also unilaterally confirm what it returned.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Compare the permission required to create and send an order with the permission required to confirm its
  finished-output receipt.
```

## G06-MRP_SUBCONTRACTING-Q049

```yaml
QID: G06-MRP_SUBCONTRACTING-Q049
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The record of a finished-output receipt from an outside party captures who confirmed it and when, in a way that
  remains visible for later review, rather than the confirming identity being overwritable or indistinguishable
  from the order's original creator.
WHY_IT_MATTERS: >
  Without a durable record of who actually confirmed physical receipt, no one can later establish whose word the
  organisation is relying on for something none of its own staff observed being made.
DISCONFIRMING_OBSERVATION: >
  The identity and timestamp of whoever confirmed a finished-output receipt cannot be retrieved afterward, or can
  be silently overwritten by a later action.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Confirm a finished-output receipt as one user, then attempt to retrieve who confirmed it and when at a later
  time.
```

## G06-MRP_SUBCONTRACTING-Q050

```yaml
QID: G06-MRP_SUBCONTRACTING-Q050
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A finished-output receipt can require a distinct quality or inspection acknowledgment step, separate from the
  quantity-receipt step, and the system does not force treating "quantity arrived" as equivalent to "quality
  accepted."
WHY_IT_MATTERS: >
  Collapsing the two steps into one would mean accepting a quantity into saleable stock is treated as an implicit,
  unreviewed quality sign-off on work the organisation never watched being performed.
DISCONFIRMING_OBSERVATION: >
  There is no way to configure or record a quality acknowledgment for a receipt from an outside party that is
  distinct from simply recording that a quantity arrived.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Attempt to configure a separate quality acknowledgment step for a finished-output receipt, distinct from
  recording the arrived quantity.
```

## G06-MRP_SUBCONTRACTING-Q051

```yaml
QID: G06-MRP_SUBCONTRACTING-Q051
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A finished-output receipt confirmed by one user can be reversed or corrected through a visible, traceable action,
  rather than the only remedy for a mistaken confirmation being to silently edit the original record.
WHY_IT_MATTERS: >
  Silent correction of a confirmation about something no one in the organisation directly observed removes the
  only trail that could later explain why the record changed.
DISCONFIRMING_OBSERVATION: >
  Correcting a mistaken finished-output receipt confirmation is done by editing the original record directly,
  leaving no trace that it was ever different.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Record a mistaken finished-output receipt confirmation and attempt to correct it, checking whether the
  correction leaves a visible trace.
```

## G06-MRP_SUBCONTRACTING-Q052

```yaml
QID: G06-MRP_SUBCONTRACTING-Q052
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  The record trail for an order distinguishes, for its component consumption figures, between a quantity the
  outside party actually reported and a quantity the system calculated by assuming the bill of materials was
  followed exactly.
WHY_IT_MATTERS: >
  An organisation reviewing the record needs to know whether a number reflects what actually happened or only what
  should have happened if nothing went wrong.
DISCONFIRMING_OBSERVATION: >
  A calculated, assumed consumption figure and an actually reported consumption figure appear identically in the
  record with no indication of which kind either one is.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Produce one consumption figure by calculation and one by direct outside-party report, and compare how each is
  labelled in the record.
```

## G06-MRP_SUBCONTRACTING-Q053

```yaml
QID: G06-MRP_SUBCONTRACTING-Q053
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  When no independent confirmation from the outside party exists at all, and the order's completion rests solely
  on the sender's own inferred assumption that the standard process was followed, that fact is discoverable from
  the record rather than the record looking identical to one backed by an actual confirmation.
WHY_IT_MATTERS: >
  A record that looks equally confident whether or not it was ever externally corroborated gives false assurance
  about how much the organisation actually knows.
DISCONFIRMING_OBSERVATION: >
  An order completed with no independent confirmation from the outside party at any point is not distinguishable,
  from its own record, from one where confirmation was actually captured.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete an order with no independent outside-party confirmation captured and compare its record with one where
  confirmation was captured.
```

## G06-MRP_SUBCONTRACTING-Q054

```yaml
QID: G06-MRP_SUBCONTRACTING-Q054
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A full history of every event recorded against a given order — every send, return, receipt, and correction — can
  be retrieved in chronological sequence as a single trail, rather than the individual events being scattered with
  no way to reconstruct the order's overall history.
WHY_IT_MATTERS: >
  A relationship that spans time and multiple partial events is exactly the situation where a scattered,
  unreconstructable history does the most damage to any later investigation.
DISCONFIRMING_OBSERVATION: >
  There is no way to retrieve the full chronological sequence of events for a given order as a single connected
  trail.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Generate several send, return, and receipt events against one order over time, then attempt to retrieve its full
  chronological history as one trail.
```

## G06-MRP_SUBCONTRACTING-Q055

```yaml
QID: G06-MRP_SUBCONTRACTING-Q055
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  The system does not present an order as fully and successfully closed while any of its component sends still
  carry an outstanding, unresolved balance; a genuine open discrepancy blocks or visibly flags a clean closure
  rather than being silently dropped.
WHY_IT_MATTERS: >
  Allowing a clean closure over an unresolved discrepancy would let a real, unaccounted-for loss disappear behind a
  status that claims everything was fine.
DISCONFIRMING_OBSERVATION: >
  An order can be marked fully closed while a component send under it still shows an outstanding, unreturned,
  unconsumed balance.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Attempt to close an order while a component send under it still carries an outstanding balance and check whether
  the closure is blocked or flagged.
```

## G06-MRP_SUBCONTRACTING-Q056

```yaml
QID: G06-MRP_SUBCONTRACTING-Q056
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Where the organisation has configured no mechanism at all to receive any information from the outside party
  about what actually happened during production — no reported consumption, no reported timing, nothing — that
  configuration state is itself visible and identifiable, rather than looking, from the outside, the same as a
  fully instrumented arrangement that simply had nothing unusual to report.
WHY_IT_MATTERS: >
  If a total absence of visibility looks the same as clean, uneventful visibility, nobody is ever prompted to ask
  what evidence the organisation actually has for what happened at a party it does not control.
DISCONFIRMING_OBSERVATION: >
  An arrangement with no outside-party reporting configured at all cannot be distinguished, from the resulting
  order records, from an arrangement with full reporting that happened to show no exceptions.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Compare the resulting order records of an arrangement with no outside-party reporting configured against one
  with full reporting configured and no exceptions to report.
```

## G06-MRP_SUBCONTRACTING-Q057

```yaml
QID: G06-MRP_SUBCONTRACTING-Q057
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  The quantity of a component recorded as sent against an order cannot be driven negative by a return or
  consumption event that exceeds what was actually sent; such an event is rejected or flagged rather than silently
  accepted as a negative outstanding balance.
WHY_IT_MATTERS: >
  A negative outstanding balance is not a physically meaningful state, and its silent acceptance signals an
  order-of-operations defect that would corrupt anyone's reconciliation.
DISCONFIRMING_OBSERVATION: >
  A return or consumption record can be entered for a quantity exceeding what remains outstanding, producing a
  negative outstanding balance with no rejection or exception raised.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Attempt to record a return or consumption quantity larger than the remaining outstanding balance for a component
  and check whether it is accepted.
```

## G06-MRP_SUBCONTRACTING-Q058

```yaml
QID: G06-MRP_SUBCONTRACTING-Q058
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Two separate users recording a return and a receipt against the same outstanding component balance at nearly the
  same time both have their events correctly reflected in the resulting balance, rather than one event silently
  overwriting or being lost because of the other's concurrent update.
WHY_IT_MATTERS: >
  A lost concurrent update on a shared outstanding balance would misstate the true position with no indication
  anything was ever dropped.
DISCONFIRMING_OBSERVATION: >
  Recording two nearly simultaneous events against the same outstanding component balance results in one of them
  not being reflected in the final balance at all.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Have two users record nearly simultaneous events against the same outstanding component balance and check
  whether both are reflected in the final balance.
```

## G06-MRP_SUBCONTRACTING-Q059

```yaml
QID: G06-MRP_SUBCONTRACTING-Q059
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Stock held at an outside party is attributed to the same operating company or branch scope that owned the
  components before they were sent, so an outside party used across more than one company or branch does not allow
  one scope's components to be reported under another's ownership.
WHY_IT_MATTERS: >
  Blurring company or branch attribution at a shared outside party would misstate each scope's own asset position
  and could let one branch's loss be absorbed, invisibly, by another's figures.
DISCONFIRMING_OBSERVATION: >
  Components sent to an outside party by one company or branch scope can appear as outstanding stock belonging to a
  different scope that shares the same outside party relationship.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Send components from two different company or branch scopes to the same shared outside party and check whether
  each scope's outstanding stock stays correctly attributed.
```

## G06-MRP_SUBCONTRACTING-Q060

```yaml
QID: G06-MRP_SUBCONTRACTING-Q060
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  An arrangement, once configured with a bill of materials and an outside party, can actually be carried through
  send, partial events, and receipt to a genuine closed state in the running system, rather than the configuration
  existing on paper while some required step is in practice unreachable.
WHY_IT_MATTERS: >
  A configuration that looks complete but cannot actually be completed end to end would only be discovered when a
  real order gets stuck, at the worst possible time.
DISCONFIRMING_OBSERVATION: >
  A fully configured arrangement cannot be carried through to an actual closed order in the running system; some
  required step has no way to be performed.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Configure a complete arrangement and attempt to carry one order through every step to a genuine closed state.
```

## G06-MRP_SUBCONTRACTING-Q061

```yaml
QID: G06-MRP_SUBCONTRACTING-Q061
MODULE: mrp_subcontracting
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  The component quantity an order expects to send is recalculated correctly when the order's own finished-output
  quantity is changed before any components have gone out, rather than retaining a component quantity calculated
  for the original, now-superseded order quantity.
WHY_IT_MATTERS: >
  Sending a component quantity based on a stale order size either strands unneeded material at the outside party or
  under-supplies what the revised order actually needs.
DISCONFIRMING_OBSERVATION: >
  Changing an order's finished-output quantity before any components are sent does not change the component
  quantity the system expects to send.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change an order's finished-output quantity before sending any components and check whether the expected
  component quantity is recalculated.
```

---
## GMVQ Internal QA Checklist

- [x] 61 distinct MVQ records (exceeds the 48 floor; no padding — every record targets a distinct hypothesis).
- [x] Every record has a concrete `DISCONFIRMING_OBSERVATION`.
- [x] Questions are behavioral and source-neutral; no vendor/product name, technical identifier, or module name
      appears in question text.
- [x] Ownership and location of stock at an outside party represented (Q001-Q005).
- [x] Components sent and never returned, returned short, returned as a different item, or diverted to another
      order represented (Q006-Q011).
- [x] Finished-output receipt without evidence of matching component consumption represented (Q012-Q015).
- [x] Bill of materials as the record of expected consumption, and resupply vs self-sourced arrangements,
      represented (Q016-Q020).
- [x] Scrap and yield loss occurring out of sight, and its attribution, represented (Q021-Q024).
- [x] Lot and serial traceability across the boundary represented (Q025-Q028).
- [x] The outside party's own timing versus the sender's recorded timing represented (Q029-Q031).
- [x] Cancellation while components are physically at the outside party represented (Q032-Q035).
- [x] Partial return against a partially consumed send represented (Q036-Q039).
- [x] The outside party relationship ending or becoming unreachable with stock still in place represented
      (Q040-Q043).
- [x] Period close with components out and nothing back yet represented (Q044-Q047).
- [x] Authority to confirm receipt of unobserved production represented (Q048-Q051).
- [x] What evidence of production exists at all, and whether the record admits it is inferred, represented
      (Q052-Q056).
- [x] Negative-balance, concurrency, company/branch boundary, and configuration-reachability represented
      (Q057-Q061).
- [x] Ledger treatment, the commercial/purchase document, dropshipped output, later-arriving cost, and the repair
      loop are excluded and recorded against their owning sibling bank (see Control section).
- [ ] Independent QA challenge outcome recorded.
- [ ] SaaS Architecture challenge outcome recorded.
- [ ] Rolling batch freeze recorded before Lane A/Lane B.

**Disposition:** AUTHORING COMPLETE FOR THIS DRAFT / QA CHALLENGE NEXT
