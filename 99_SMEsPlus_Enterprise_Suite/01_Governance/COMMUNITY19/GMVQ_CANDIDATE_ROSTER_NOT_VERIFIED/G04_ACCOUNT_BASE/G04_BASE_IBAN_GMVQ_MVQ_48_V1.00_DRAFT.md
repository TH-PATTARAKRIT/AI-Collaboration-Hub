# SMEsPlus ENTERPRISE SUITE
## GMVQ — G04 ACCOUNT_BASE / base_iban Module MVQ Bank

**Document ID:** GMVQ-G04-BASE_IBAN-MVQ48-V1.00
**Group:** G04 ACCOUNT_BASE (Wave W1)
**Module Metadata:** `base_iban`
**Wave:** W1
**Author Cell:** TEAM 22 (GMVQ Question Factory — Internal Production Team 22, Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies the module-specific (MVQ) tier for structured bank account identifiers and their
validation. Per the Group G04 brief this sits in the highest-risk group in the programme: bank
identifier handling is the classic surface for payment-redirection fraud, so the material ground is
format validation versus actual account existence, identifier changes after payments have already
been issued, selection among multiple accounts, cross-entity and cross-company boundaries, masking,
concurrency, and the audit trail of a bank-detail change.

Question text is source-neutral. It does not name the module, any vendor or product, or any
technical identifier (field, model, method, XML ID, API path). The generic term "structured bank
account identifier" is used throughout in place of any specific standard's name.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: 48 questions exist because each tests a distinct material hypothesis, spread across
  the required dimensions (business rule, state transition, configuration dependency, role and
  permission, exception path, cancellation, reversal, negative case, cross-module dependency,
  auditability, tenant/company boundary, concurrency and ordering, runtime reachability).
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only. No Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not MASTER-ready.

## G04-BASE_IBAN-Q001

```yaml
QID: G04-BASE_IBAN-Q001
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Format and check-digit validation confirms only structural validity, and the system does not treat
  a structurally valid identifier as proof that the underlying account actually exists or is
  reachable.
WHY_IT_MATTERS: >
  Treating structural validity as proof of existence gives false confidence that a payee's account
  is real when it has never actually been confirmed.
DISCONFIRMING_OBSERVATION: >
  On accepting a structurally valid identifier, the system presents or logs any indication that the
  account itself has been confirmed to exist.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Enter a structurally valid but fabricated identifier and observe any language, status, or log
  entry suggesting existence was confirmed.
```

## G04-BASE_IBAN-Q002

```yaml
QID: G04-BASE_IBAN-Q002
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Country-specific structural rules are enforced consistently at every entry point — interactive
  form, bulk import, and integration — not only at the primary interactive form.
WHY_IT_MATTERS: >
  A validation rule that only applies on one path is not a control; it is a control with a known
  bypass.
DISCONFIRMING_OBSERVATION: >
  An identifier that fails structural validation through the interactive form is accepted through
  import or integration.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Attempt the same invalid identifier through the interactive path, then through import, then
  through integration, and compare outcomes.
```

## G04-BASE_IBAN-Q003

```yaml
QID: G04-BASE_IBAN-Q003
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Bulk import does not provide a path to bypass the check-digit validation that the interactive path
  enforces.
WHY_IT_MATTERS: >
  Import is a common route for onboarding many payees at once; a bypass there defeats the control at
  the point of highest volume.
DISCONFIRMING_OBSERVATION: >
  An import file containing a checksum-invalid identifier is accepted without rejection or without
  at least a warning equivalent to the interactive path's rejection.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Construct an import file containing a checksum-invalid identifier and import it.
```

## G04-BASE_IBAN-Q004

```yaml
QID: G04-BASE_IBAN-Q004
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An identifier's format validity is checked both at the time it is saved and, independently, on
  already-stored data on a periodic or on-demand basis, so records predating a validation rule
  change are eventually caught.
WHY_IT_MATTERS: >
  A validation rule introduced after data already exists is worthless if nothing ever re-checks the
  data that predates it.
DISCONFIRMING_OBSERVATION: >
  No mechanism exists to re-check previously stored identifiers after a validation rule is
  introduced or tightened, and known-invalid legacy records go undetected indefinitely.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Introduce or tighten a validation rule and check whether existing records are re-evaluated by any
  available means.
```

## G04-BASE_IBAN-Q005

```yaml
QID: G04-BASE_IBAN-Q005
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A country format not covered by an explicit validation rule is handled by a defined, consistent
  fallback (permissive pass-through with a flag, or a block), not an undefined and inconsistent
  behaviour.
WHY_IT_MATTERS: >
  Inconsistent handling of uncovered formats means the same input can be silently accepted one time
  and silently rejected another, with no way to predict which.
DISCONFIRMING_OBSERVATION: >
  Entering an identifier for an uncovered country format produces inconsistent outcomes across
  repeated attempts or across entry points.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Identify a country format without an explicit rule and test entry behaviour multiple times and
  through multiple paths.
```

## G04-BASE_IBAN-Q006

```yaml
QID: G04-BASE_IBAN-Q006
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Changing a partner's stored identifier does not alter the identifier recorded on a payment already
  issued; the historical payment record retains the identifier that was actually in effect at the
  time of payment.
WHY_IT_MATTERS: >
  A payment history that silently rewrites itself to match the current identifier destroys the
  ability to reconstruct what actually happened at the time money moved.
DISCONFIRMING_OBSERVATION: >
  After editing a partner's identifier, a previously issued payment's record displays the new
  identifier rather than the one in effect when it was issued.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Issue a payment against a stored identifier, then edit the identifier, then inspect the historical
  payment record.
```

## G04-BASE_IBAN-Q007

```yaml
QID: G04-BASE_IBAN-Q007
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Every creation, modification, and deactivation of a stored identifier produces its own distinct
  audit entry, rather than being inferred from the partner record's general change history.
WHY_IT_MATTERS: >
  Bank-detail changes are a specific, high-risk category of edit that a reviewer needs to find
  directly, not by sifting through unrelated partner edits.
DISCONFIRMING_OBSERVATION: >
  An identifier change occurred but there is no audit entry specific to that field distinguishable
  from unrelated partner-record edits.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Change only the identifier on a partner record and inspect the audit trail for a field-specific
  entry.
```

## G04-BASE_IBAN-Q008

```yaml
QID: G04-BASE_IBAN-Q008
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where an identifier change is expected to require separate approval, the audit trail distinguishes
  who entered the change from who approved it.
WHY_IT_MATTERS: >
  A single-actor trail cannot demonstrate that a four-eyes control was actually exercised rather than
  nominally configured.
DISCONFIRMING_OBSERVATION: >
  The audit trail records only a single actor for a change, with no way to tell whether entry and
  approval were the same person or different people.
EXPECTED_SURFACE: S6,S4
PRECONDITIONS: >
  Perform an identifier change under a workflow expected to require separate approval and inspect
  what the trail actually distinguishes.
```

## G04-BASE_IBAN-Q009

```yaml
QID: G04-BASE_IBAN-Q009
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A change to a payee's identifier does not silently take effect for a payment that was already
  queued or already approved before the change, without that payment being re-surfaced for review.
WHY_IT_MATTERS: >
  This is the exact mechanism of payment-redirection fraud: change the destination after approval,
  before the money actually moves.
DISCONFIRMING_OBSERVATION: >
  A payment approved before the identifier change is executed automatically using the new identifier
  with no re-review step.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Approve a payment, then change the payee's identifier before the payment executes, and observe
  what identifier is actually used.
```

## G04-BASE_IBAN-Q010

```yaml
QID: G04-BASE_IBAN-Q010
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An identifier change occurring during an active payment run is not picked up mid-run by that same
  run; the run either uses the value as it stood when the run started, or halts and flags the
  affected item.
WHY_IT_MATTERS: >
  A run that silently switches identifiers mid-flight produces an outcome no single point-in-time
  review could have anticipated or authorized.
DISCONFIRMING_OBSERVATION: >
  A payment run in progress silently switches to a newly edited identifier partway through its own
  execution with no flag.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Start a payment run covering a given payee, and edit that payee's identifier while the run is
  executing.
```

## G04-BASE_IBAN-Q011

```yaml
QID: G04-BASE_IBAN-Q011
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A single account cannot both change a payee's identifier and approve or execute a payment to that
  same payee without a documented compensating control.
WHY_IT_MATTERS: >
  Combining the ability to redirect a payment with the ability to approve it removes the separation
  of duties the whole payment control model depends on.
DISCONFIRMING_OBSERVATION: >
  A single account can both change a payee's identifier and approve or execute a payment to that
  payee with no separation of duties or compensating check.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Attempt both actions — identifier change and payment approval/execution to the same payee — from a
  single account with combined access.
```

## G04-BASE_IBAN-Q012

```yaml
QID: G04-BASE_IBAN-Q012
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a partner has more than one active identifier, the one selected for a given payment follows
  an explicit, discoverable rule — an explicit default, or a required selection at transaction time
  — not an undocumented "most recent" or arbitrary pick.
WHY_IT_MATTERS: >
  An unpredictable selection rule among several valid accounts is itself a risk, independent of
  whether any single account is compromised.
DISCONFIRMING_OBSERVATION: >
  Two payments to the same partner with multiple active identifiers, made under identical
  conditions, use different identifiers with no explicit reason recorded.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Set up a partner with two active identifiers and issue two payments under otherwise identical
  conditions.
```

## G04-BASE_IBAN-Q013

```yaml
QID: G04-BASE_IBAN-Q013
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A manual override of the default identifier selection at transaction time is recorded distinctly
  from an ordinary default-following payment.
WHY_IT_MATTERS: >
  An override deserves more scrutiny than a default selection, but only if it can actually be found
  as an override afterward.
DISCONFIRMING_OBSERVATION: >
  A payment that used a non-default identifier shows no distinguishing record from one that used the
  default.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Issue one payment using the default identifier and one using a manual override, and compare their
  records.
```

## G04-BASE_IBAN-Q014

```yaml
QID: G04-BASE_IBAN-Q014
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An identifier registered to a different legal entity than the stated payee is detectable as a
  mismatch, rather than accepted silently because the identifier itself is structurally valid.
WHY_IT_MATTERS: >
  Structural validity says nothing about whether the account belongs to the party being paid; this
  is a distinct and higher-value check.
DISCONFIRMING_OBSERVATION: >
  A payment proceeds using an identifier registered to an entity other than the stated payee, with
  no warning surfaced anywhere in the flow.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attach an identifier known to belong to a different legal entity to a payee record and attempt a
  payment.
```

## G04-BASE_IBAN-Q015

```yaml
QID: G04-BASE_IBAN-Q015
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A partner's stored identifiers are scoped for visibility according to company boundaries in a
  multi-company environment; access to a partner in one company context does not expose identifiers
  entered under a different company's context.
WHY_IT_MATTERS: >
  Bank details are exactly the kind of sensitive, company-owned data that a tenant/company boundary
  is meant to protect.
DISCONFIRMING_OBSERVATION: >
  A user with access limited to one company can view or select an identifier entered under a
  different company's context.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create the same partner with distinct identifiers under two company contexts and check
  cross-context visibility for a company-scoped user.
```

## G04-BASE_IBAN-Q016

```yaml
QID: G04-BASE_IBAN-Q016
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A payment executed under one company's context cannot draw on or write to an identifier record
  scoped to a different company without an explicit, authorized cross-company action.
WHY_IT_MATTERS: >
  A cross-company leak in payment routing data is a boundary failure with direct financial
  consequence, not merely a visibility inconvenience.
DISCONFIRMING_OBSERVATION: >
  A payment issued in one company context uses or modifies an identifier record scoped to another
  company with no explicit cross-company authorization step.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt a payment in one company context referencing an identifier scoped to another company.
```

## G04-BASE_IBAN-Q017

```yaml
QID: G04-BASE_IBAN-Q017
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Full identifiers are masked (partially obscured) wherever they appear in exports intended for
  general handling, not shown in full by default.
WHY_IT_MATTERS: >
  An unmasked export multiplies the number of places a payment identifier can leak far beyond the
  system's own access controls.
DISCONFIRMING_OBSERVATION: >
  A routine export intended for general handling contains the full, unmasked identifier where
  masking would be expected.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Produce a standard export containing partner payment details and inspect how the identifier is
  rendered.
```

## G04-BASE_IBAN-Q018

```yaml
QID: G04-BASE_IBAN-Q018
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Full identifiers are masked in printed payment-related documents, such as remittance advice,
  unless a specific document's purpose explicitly requires the full value.
WHY_IT_MATTERS: >
  A printed document circulates further and is harder to control than an on-screen view.
DISCONFIRMING_OBSERVATION: >
  A printed document not specifically requiring the full identifier displays it unmasked.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Generate a printed payment-related document and inspect identifier rendering.
```

## G04-BASE_IBAN-Q019

```yaml
QID: G04-BASE_IBAN-Q019
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Full identifiers do not appear in error messages, system logs, or diagnostic output presented to a
  general user.
WHY_IT_MATTERS: >
  Logs and error text are commonly copied into tickets, screenshots, and chat messages with far less
  care than the primary record itself.
DISCONFIRMING_OBSERVATION: >
  An error condition involving an identifier displays the full value in a message visible to a
  general user, rather than a masked or truncated form.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Trigger a validation error on an identifier field and inspect the exact error text shown.
```

## G04-BASE_IBAN-Q020

```yaml
QID: G04-BASE_IBAN-Q020
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A rejection message explaining why a specific identifier was invalid does not reveal enough about
  the internal validation rule to make it easy to construct a passing but fraudulent identifier by
  trial and error.
WHY_IT_MATTERS: >
  An overly specific rejection message can function as an oracle that helps an attacker craft a
  value that passes format checks while still being fraudulent.
DISCONFIRMING_OBSERVATION: >
  The rejection message specifies the exact rule violated in enough detail to reverse-engineer a
  passing value without independent knowledge of the country's format standard.
EXPECTED_SURFACE: S3
PRECONDITIONS: >
  Submit several invalid variants and compare how specific each rejection message is.
```

## G04-BASE_IBAN-Q021

```yaml
QID: G04-BASE_IBAN-Q021
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Two users editing the same partner's identifier concurrently do not result in one edit being
  silently lost with no conflict indication.
WHY_IT_MATTERS: >
  A silently lost edit on payment-routing data can leave a record in a state nobody actually chose.
DISCONFIRMING_OBSERVATION: >
  Two concurrent edits to the same identifier field result in one change disappearing with neither
  user notified of a conflict.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Open the same partner record in two sessions and submit conflicting identifier edits at nearly the
  same time.
```

## G04-BASE_IBAN-Q022

```yaml
QID: G04-BASE_IBAN-Q022
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An identifier that has been deactivated or archived cannot be selected for a new payment through
  any available path, including one that bypasses the normal active-record filter.
WHY_IT_MATTERS: >
  A deactivated identifier that can still be reached defeats the purpose of deactivating it in the
  first place.
DISCONFIRMING_OBSERVATION: >
  A deactivated identifier can still be selected and used for a new payment through some available
  path.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Deactivate an identifier and attempt to select it for a new payment through every available entry
  path.
```

## G04-BASE_IBAN-Q023

```yaml
QID: G04-BASE_IBAN-Q023
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Deactivating or archiving an identifier does not alter how historical payments that used it are
  displayed or reported; the historical record remains intact and attributable.
WHY_IT_MATTERS: >
  Historical accuracy must not depend on the current active/inactive status of a record it once
  referenced.
DISCONFIRMING_OBSERVATION: >
  Historical payment records lose or alter their identifier reference after the identifier itself is
  deactivated.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Deactivate an identifier that has payment history and inspect that history afterward.
```

## G04-BASE_IBAN-Q024

```yaml
QID: G04-BASE_IBAN-Q024
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deleting an identifier record that has associated payment history is prevented, or requires an
  explicit override distinct from ordinary deactivation, since deletion — unlike deactivation — can
  remove the historical reference itself.
WHY_IT_MATTERS: >
  Deletion of a record with payment history destroys evidence in a way deactivation does not.
DISCONFIRMING_OBSERVATION: >
  An identifier with payment history can be deleted outright through the same action used for one
  with no history, with no distinguishing safeguard.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt to delete an identifier with payment history and one without, and compare the paths and
  any safeguards encountered.
```

## G04-BASE_IBAN-Q025

```yaml
QID: G04-BASE_IBAN-Q025
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a validation step depends on an external registry or lookup service, an outage or
  unreachability of that service produces an explicit, distinguishable status rather than silently
  falling back to treating the identifier as either fully valid or fully invalid.
WHY_IT_MATTERS: >
  Collapsing "could not verify" into "verified" or "rejected" hides exactly the uncertainty a
  reviewer most needs to see.
DISCONFIRMING_OBSERVATION: >
  When the external service is unreachable, the result is indistinguishable from a normal pass or a
  normal fail, with no "unable to verify" state recorded.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Simulate the external validation service being unreachable and attempt to save an identifier.
```

## G04-BASE_IBAN-Q026

```yaml
QID: G04-BASE_IBAN-Q026
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An identifier saved while the external verification step was unreachable is flagged for later
  re-verification, rather than treated as permanently confirmed.
WHY_IT_MATTERS: >
  A record saved under uncertainty that is never revisited becomes indistinguishable from one that
  was actually verified.
DISCONFIRMING_OBSERVATION: >
  An identifier saved during an outage is never revisited and remains indistinguishable from one
  that was actually externally verified.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Save an identifier during a simulated outage, restore the service, and check whether anything
  prompts re-verification.
```

## G04-BASE_IBAN-Q027

```yaml
QID: G04-BASE_IBAN-Q027
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The currency associated with a stored identifier's account, where recorded, is checked for
  consistency against the currency of a payment made to it, at least to the extent of a warning on
  mismatch.
WHY_IT_MATTERS: >
  A currency mismatch is often a sign that the wrong account, or the wrong record entirely, has been
  selected.
DISCONFIRMING_OBSERVATION: >
  A payment in a currency inconsistent with the recorded account currency proceeds with no warning.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Set a recorded account currency, then issue a payment in a different currency to the same
  identifier.
```

## G04-BASE_IBAN-Q028

```yaml
QID: G04-BASE_IBAN-Q028
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Formatting variants of the same physical identifier, differing only in spacing or letter case, are
  normalized so they are treated as the same identifier for duplicate-detection purposes.
WHY_IT_MATTERS: >
  A duplicate-detection control that a cosmetic difference can defeat gives no real protection.
DISCONFIRMING_OBSERVATION: >
  Two entries differing only in spacing or case are treated as distinct identifiers, defeating
  duplicate detection.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Enter the same identifier twice with only formatting differences and check duplicate detection.
```

## G04-BASE_IBAN-Q029

```yaml
QID: G04-BASE_IBAN-Q029
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Bank statement reconciliation matching against a stored identifier tolerates the same formatting
  variants; a purely cosmetic difference does not cause an otherwise-correct match to fail.
WHY_IT_MATTERS: >
  A reconciliation failure caused only by formatting forces manual review that can mask a genuine
  mismatch underneath a pile of cosmetic ones.
DISCONFIRMING_OBSERVATION: >
  Reconciliation fails to match an otherwise correct identifier solely due to spacing or case
  difference.
EXPECTED_SURFACE: S2,S3
PRECONDITIONS: >
  Run reconciliation where the statement-side identifier differs only cosmetically from the stored
  one.
```

## G04-BASE_IBAN-Q030

```yaml
QID: G04-BASE_IBAN-Q030
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The identical identifier value is not silently permitted as the active default for two different
  partners at the same time without at least a flag.
WHY_IT_MATTERS: >
  The same account serving as the recognized default for two unrelated partners is a classic
  indicator of a redirection error or fraud.
DISCONFIRMING_OBSERVATION: >
  Two distinct partner records carry the identical active identifier as their default with no flag
  raised anywhere.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Set the identical identifier as the active default on two different partner records.
```

## G04-BASE_IBAN-Q031

```yaml
QID: G04-BASE_IBAN-Q031
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A different identifier value referenced only informally, such as in an attached note or free-text
  field, does not become the effective payment identifier without an explicit, separate update
  action in the defined field.
WHY_IT_MATTERS: >
  If a value mentioned in a note can silently become the operative payment destination, the defined
  change workflow and its controls can be sidestepped entirely.
DISCONFIRMING_OBSERVATION: >
  An identifier value present only in an attached note or free-text field becomes the effective
  payment identifier without an explicit, separate update action in the defined field.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attach a document or note referencing a different identifier and check whether the live payment
  identifier changes as a result.
```

## G04-BASE_IBAN-Q032

```yaml
QID: G04-BASE_IBAN-Q032
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a waiting or verification period is defined for identifier changes, a change made
  immediately before a scheduled payment run is still subject to it, rather than bypassing it
  because the run happened to fall inside the window.
WHY_IT_MATTERS: >
  A waiting period that a well-timed change can skip provides no real protection against
  last-minute redirection.
DISCONFIRMING_OBSERVATION: >
  A change made just before a scheduled run's cutoff is used by that run despite a defined waiting
  period that should have deferred it.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Where a waiting period exists, make a change just before a run's cutoff and observe whether the
  run respects or bypasses it.
```

## G04-BASE_IBAN-Q033

```yaml
QID: G04-BASE_IBAN-Q033
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The permission to change a payee's identifier is distinguishable from, and separately grantable
  from, the general permission to edit a partner record.
WHY_IT_MATTERS: >
  Bundling identifier changes into general edit rights means anyone who can update a partner's
  address can also redirect their payments.
DISCONFIRMING_OBSERVATION: >
  A role with general partner-edit access but no specific grant for payment-identifier changes is
  still able to change the identifier.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Where such a distinction is configurable, attempt an identifier change from an account with
  general partner-edit rights but without any distinct identifier-change grant.
```

## G04-BASE_IBAN-Q034

```yaml
QID: G04-BASE_IBAN-Q034
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Changing a payment identifier requires a distinct confirming action separate from the action that
  created the record in the first place, so a single step cannot both create and finalize a change
  to live payment routing.
WHY_IT_MATTERS: >
  A one-step create-and-activate flow for a high-risk field removes the natural pause point where a
  mistake or a fraudulent change could otherwise be caught.
DISCONFIRMING_OBSERVATION: >
  Creating and immediately activating a changed identifier for use in payment happens as a single
  undifferentiated action with no separate confirmation step.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Perform an identifier change end to end and count the distinct confirming actions required before
  it becomes usable in a payment.
```

## G04-BASE_IBAN-Q035

```yaml
QID: G04-BASE_IBAN-Q035
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Removing an identifier and later re-adding the identical value preserves a traceable link to the
  earlier record's history, rather than presenting as a brand-new, unrelated record.
WHY_IT_MATTERS: >
  Losing the link between a removed and re-added identifier could hide a pattern of removal and
  reinstatement that a reviewer would otherwise want to see together.
DISCONFIRMING_OBSERVATION: >
  Re-adding a previously removed identifier value creates a record with no traceable connection to
  the earlier one's history.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Remove an identifier, then re-add the identical value, and inspect whether prior history is linked
  or lost.
```

## G04-BASE_IBAN-Q036

```yaml
QID: G04-BASE_IBAN-Q036
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The same validation strictness applied to a master partner record's identifier also applies to a
  one-time or ad hoc payee entry used for a single payment.
WHY_IT_MATTERS: >
  A weaker check on ad hoc payees creates an easy path around the controls built for master records.
DISCONFIRMING_OBSERVATION: >
  An ad hoc, non-master payee entry accepts an identifier that would be rejected on a master partner
  record.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt the same invalid identifier on a master partner record and on a one-time payee entry.
```

## G04-BASE_IBAN-Q037

```yaml
QID: G04-BASE_IBAN-Q037
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where a single partner record is used both to receive funds (as a customer, for refunds) and to be
  paid funds (as a vendor), the identifier used for each direction is independently determined, not
  silently shared such that a change made for one direction alters the other.
WHY_IT_MATTERS: >
  Sharing one identifier field across two different payment directions means a change intended for
  one purpose can unexpectedly redirect the other.
DISCONFIRMING_OBSERVATION: >
  Changing the vendor-direction identifier also changes what is used for a customer-direction
  refund, or vice versa, with no independent control.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Configure distinct identifiers for the two directions on the same partner, change one, and check
  the other.
```

## G04-BASE_IBAN-Q038

```yaml
QID: G04-BASE_IBAN-Q038
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A report listing every identifier change across a period, independent of any specific partner's
  own history view, can be obtained for periodic review.
WHY_IT_MATTERS: >
  Periodic review of this specific, high-risk change category should not depend on visiting every
  partner record individually.
DISCONFIRMING_OBSERVATION: >
  There is no way to obtain a period-wide list of identifier changes across all partners without
  visiting each partner record individually.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Attempt to produce a period-wide change report and see what is available.
```

## G04-BASE_IBAN-Q039

```yaml
QID: G04-BASE_IBAN-Q039
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A historical payment document, when viewed or reprinted later, shows the identifier as it stood at
  the time of that payment, not the partner's currently stored identifier if it has since changed.
WHY_IT_MATTERS: >
  A reprinted document that quietly reflects today's data rather than what was actually used at the
  time misrepresents the historical transaction.
DISCONFIRMING_OBSERVATION: >
  Reprinting a historical payment document shows the current identifier rather than the one used at
  the time of the original payment.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change a partner's identifier after a payment, then reprint or re-view that historical payment
  document.
```

## G04-BASE_IBAN-Q040

```yaml
QID: G04-BASE_IBAN-Q040
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where an identifier's country-of-issue implies a specific jurisdiction, a mismatch between that
  implied jurisdiction and the payee's recorded jurisdiction is at least flagged, not passed through
  silently.
WHY_IT_MATTERS: >
  A jurisdiction mismatch between a payee's own records and the account they are supposedly paid
  through is a plausible early signal of a redirection attempt.
DISCONFIRMING_OBSERVATION: >
  An identifier whose implied jurisdiction clearly differs from the payee's recorded jurisdiction is
  accepted with no flag.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Attach an identifier with a clearly mismatched country-of-issue to a payee record and observe
  whether anything is flagged.
```

## G04-BASE_IBAN-Q041

```yaml
QID: G04-BASE_IBAN-Q041
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The set of supported country formats and their validation rules is itself maintained in a
  versioned way, so a later dispute about why a given identifier was accepted or rejected at a point
  in time can be resolved.
WHY_IT_MATTERS: >
  Without a versioned ruleset, a past acceptance or rejection cannot be explained or defended after
  the rules have since changed.
DISCONFIRMING_OBSERVATION: >
  There is no way to determine which validation ruleset was in effect at a past point in time when a
  given identifier was accepted.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Change the validation ruleset, then attempt to determine what ruleset applied to an identifier
  accepted before the change.
```

## G04-BASE_IBAN-Q042

```yaml
QID: G04-BASE_IBAN-Q042
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A payment run fails closed — stopping and flagging the item — rather than failing open, when it
  cannot determine which identifier to use for a payee due to conflicting or ambiguous active
  records.
WHY_IT_MATTERS: >
  Proceeding on an arbitrary guess among ambiguous, conflicting records is worse than stopping,
  because the outcome cannot be predicted or defended afterward.
DISCONFIRMING_OBSERVATION: >
  A payment run proceeds using an arbitrarily chosen identifier when more than one active,
  differently valued identifier exists with no clear default.
EXPECTED_SURFACE: S2,S8
PRECONDITIONS: >
  Create an ambiguous multi-identifier situation with no explicit default and run a payment through
  it.
```

## G04-BASE_IBAN-Q043

```yaml
QID: G04-BASE_IBAN-Q043
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An identifier change initiated through an integration or automated feed is subject to the same
  approval and audit requirements as one entered interactively, not treated as pre-trusted because
  it arrived programmatically.
WHY_IT_MATTERS: >
  An automated feed is not an inherently trustworthy source; it is simply a different entry point
  that deserves the same scrutiny.
DISCONFIRMING_OBSERVATION: >
  An identifier change submitted through an automated integration takes effect with less scrutiny —
  no approval step, no audit entry — than the same change made interactively.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Submit an identifier change through an integration path and compare its resulting approval and
  audit trail to an interactive equivalent.
```

## G04-BASE_IBAN-Q044

```yaml
QID: G04-BASE_IBAN-Q044
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A bulk update affecting many partners' identifiers in one operation produces a per-record audit
  entry for each affected partner, not a single undifferentiated bulk-action log line.
WHY_IT_MATTERS: >
  A single generic log line for a bulk change makes it impossible to review which specific payees
  and values actually changed.
DISCONFIRMING_OBSERVATION: >
  A bulk update affecting many partners' identifiers produces one generic log entry with no way to
  see which specific partners and values changed.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Perform a bulk identifier update across several partners and inspect the resulting audit detail.
```

## G04-BASE_IBAN-Q045

```yaml
QID: G04-BASE_IBAN-Q045
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A payee record with a blank or incomplete identifier field blocks a payment attempt against it,
  rather than allowing the payment to proceed through some other unintended routing.
WHY_IT_MATTERS: >
  A payment that proceeds despite missing routing data must be going somewhere; that somewhere needs
  to be an explicit operator choice, not a silent fallback.
DISCONFIRMING_OBSERVATION: >
  A payment to a payee with no valid stored identifier still proceeds, routed by some fallback the
  operator did not explicitly choose.
EXPECTED_SURFACE: S2,S3
PRECONDITIONS: >
  Attempt a payment to a payee with a blank or incomplete identifier field.
```

## G04-BASE_IBAN-Q046

```yaml
QID: G04-BASE_IBAN-Q046
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Merging two partner records believed to represent the same entity surfaces a conflict, rather than
  silently choosing one side's identifier as authoritative, when both sides carry different active
  identifiers.
WHY_IT_MATTERS: >
  A silent choice between two conflicting payment identifiers during a merge could quietly discard
  the one that was actually correct.
DISCONFIRMING_OBSERVATION: >
  Merging two partner records with differing active identifiers picks one silently with no surfaced
  conflict or choice presented.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create two partner records for the same entity with different active identifiers and merge them.
```

## G04-BASE_IBAN-Q047

```yaml
QID: G04-BASE_IBAN-Q047
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An identifier entered under a test or non-production configuration is not reachable by a live
  payment run in a production configuration under any shared-data condition.
WHY_IT_MATTERS: >
  Test data leaking into production payment processing is a boundary failure independent of whether
  the test data itself was ever meant to be sensitive.
DISCONFIRMING_OBSERVATION: >
  An identifier or its associated flag entered under a test configuration influences or appears in a
  live production payment run.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Where a test/sandbox configuration exists alongside production, enter data in the test
  configuration and check for any leakage into production payment processing.
```

## G04-BASE_IBAN-Q048

```yaml
QID: G04-BASE_IBAN-Q048
MODULE: base_iban
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The complete lifecycle of an identifier change that immediately precedes a payment to it — the
  change itself, followed shortly by a payment run reaching it — can be reconstructed end to end from
  stored evidence alone, without relying on any party's recollection.
WHY_IT_MATTERS: >
  This exact sequence is the observable signature of payment-redirection fraud; if it cannot be
  reconstructed from records alone, the audit trail has failed at its single most important job.
DISCONFIRMING_OBSERVATION: >
  The timeline of an identifier change followed shortly by a payment to it cannot be fully
  reconstructed from stored records — timestamps, actors, and the payment itself all present with
  gaps.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Perform an identifier change immediately followed by a payment run reaching it, then attempt to
  reconstruct the full timeline using only stored evidence.
```
