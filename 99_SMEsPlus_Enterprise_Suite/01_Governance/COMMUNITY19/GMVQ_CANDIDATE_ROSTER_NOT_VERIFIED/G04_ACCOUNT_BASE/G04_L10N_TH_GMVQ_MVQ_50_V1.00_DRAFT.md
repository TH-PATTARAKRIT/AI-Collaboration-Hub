# SMEsPlus ENTERPRISE SUITE
## GMVQ — G04 ACCOUNT_BASE / l10n_th Module Adversarial MVQ Bank

**Document ID:** GMVQ-G04-L10N_TH-MVQ50-V1.00
**Group:** G04 ACCOUNT_BASE
**Module Metadata:** `l10n_th`
**Wave:** W1
**Author Cell:** TEAM 24 (GMVQ Question Factory — Internal Production Team 24, Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50
**legal_tax_review_required_count:** 4
**Lane A / Lane B:** NOT STARTED for this module until rolling batch freeze is recorded

## Purpose

This bank supplies module-specific MVQ for the Thailand localisation subject matter (local chart of accounts, local tax setup, local document requirements) within the highest-risk group, G04 ACCOUNT_BASE. It targets installation and update safety onto a database already holding posted transactions, closed-period integrity, chart-collision handling, branch/head-office attribution and document series, document-type numbering and gaps, effective-dated versus retroactive tax treatment, reporting-grouping stability, reprint fidelity, language/script fidelity on printed and exported output, rounding conventions and residuals, multi-jurisdiction coexistence in one database, legacy-master-data gaps, auditability of version and configuration provenance, and the approval/execution/posting separation as it applies to locally required document types.

This bank does not assert any Thai statutory rate, form number, certificate layout, or filing deadline. Every question whose answer depends on a specific statutory rule is written behaviourally and carries `LEGAL_TAX_REVIEW_REQUIRED: YES`.

The question text is source-neutral and does not expose vendor or product names, technical identifiers (model, table, field, method, XML ID, API path), or the module's own metadata name.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` that is a failure state, not a restatement of the hypothesis.
- No padding: 50 questions exist because they test distinct material hypotheses, spread across the material-ground dimensions given in the group brief and the quality-bar dimensions in the authoring standard.
- Questions are not evidence. A later ANSWERED state requires actual artifact/evidence.
- `module + QID` is only a Research Evidence Join Key for the blind two-lane comparison.
- No statutory rate, form identifier, certificate layout, or filing deadline is asserted anywhere in this bank.
- No Formal Coverage or Boss approval is derived from this bank. This is DRAFT / PREPARED ONLY content produced by a non-approving authoring cell.

## G04-L10N_TH-Q001

```yaml
QID: G04-L10N_TH-Q001
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Installing the localisation onto a database that already holds posted transactions must not alter the recorded content of those posted transactions.
WHY_IT_MATTERS: >
  Retroactive alteration of posted history breaks the immutability that financial audit and prior filings depend on.
DISCONFIRMING_OBSERVATION: >
  Any previously posted transaction's stored values (amounts, accounts, dates, or tax lines) differ after installation completes, with no distinct correction entry recorded.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Record the full content of a set of already-posted transactions before installation, install the localisation, then compare stored content field by field.
```

## G04-L10N_TH-Q002

```yaml
QID: G04-L10N_TH-Q002
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Installing the localisation must not silently modify a tax configuration that is already attached to existing transactions.
WHY_IT_MATTERS: >
  Silent tax-configuration changes would misstate the basis under which historical transactions were taxed.
DISCONFIRMING_OBSERVATION: >
  An existing tax configuration's rate, computation rule, or account mapping differs after installation without an explicit, logged configuration change.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Capture the full definition of tax configurations already in use, install the localisation, and compare before/after definitions.
```

## G04-L10N_TH-Q003

```yaml
QID: G04-L10N_TH-Q003
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Re-applying (updating) the localisation on a database where its configuration was already customized must not reset or duplicate that customization.
WHY_IT_MATTERS: >
  Losing customization on update would silently revert deliberate configuration decisions.
DISCONFIRMING_OBSERVATION: >
  After an update, a previously customized configuration item is found reset to a default value, or duplicated as a second conflicting entry.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Customize a configuration item introduced by the localisation, trigger an update of the localisation, and inspect the item afterward.
```

## G04-L10N_TH-Q004

```yaml
QID: G04-L10N_TH-Q004
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Updating the localisation must preserve a user-established mapping between a localised chart entry and a pre-existing account.
WHY_IT_MATTERS: >
  Losing the mapping would break the link between historical postings and their local classification.
DISCONFIRMING_OBSERVATION: >
  A previously established mapping between a localised chart entry and an existing account is missing or altered after an update, with no explicit user action recorded.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Establish a mapping between a localised chart entry and an existing account, run an update of the localisation, then re-inspect the mapping.
```

## G04-L10N_TH-Q005

```yaml
QID: G04-L10N_TH-Q005
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A localisation update applied after a period has been locked must not alter or re-derive the classification of any entry dated within that locked period.
WHY_IT_MATTERS: >
  Changing a locked period's classification undermines the integrity guarantee that a lock is supposed to provide.
DISCONFIRMING_OBSERVATION: >
  An entry dated inside a locked period shows a different classification, grouping, or tax treatment after the update than it did before, with the period still shown as locked.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Lock a period containing existing entries, apply a localisation update, then compare the entries' classification before and after.
```

## G04-L10N_TH-Q006

```yaml
QID: G04-L10N_TH-Q006
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A localisation update must not change the reporting grouping already used to produce a report that was generated for a closed period.
WHY_IT_MATTERS: >
  Changing groupings retroactively would make a previously issued report irreproducible and potentially inconsistent with what was actually filed or shared.
DISCONFIRMING_OBSERVATION: >
  Regenerating the same report for the closed period after the update produces different grouping totals than the originally generated report, with no versioning that preserves the original.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Generate and retain a report for a closed period, apply a localisation update that touches reporting groupings, then regenerate the same report and compare.
```

## G04-L10N_TH-Q007

```yaml
QID: G04-L10N_TH-Q007
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  When a standard entry introduced by the localisation would collide with a pre-existing user-defined account, the collision must be surfaced for a decision rather than silently overwritten.
WHY_IT_MATTERS: >
  Silent overwrite can misdirect future postings without anyone choosing that outcome.
DISCONFIRMING_OBSERVATION: >
  A pre-existing user-defined account is replaced, merged, or renamed by the localisation's own entry with no notice or confirmation step.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Create a custom account whose identifying attributes match a standard entry the localisation would introduce, then install or update the localisation.
```

## G04-L10N_TH-Q008

```yaml
QID: G04-L10N_TH-Q008
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  However a chart-entry collision is resolved, every historical posting must continue to point to the same effective account it pointed to before resolution.
WHY_IT_MATTERS: >
  Re-pointing historical postings would silently rewrite where past transactions are considered to have landed.
DISCONFIRMING_OBSERVATION: >
  A historical posting's effective account differs after collision resolution, without a distinct correcting entry.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Create postings against an account that will collide with a localisation entry, resolve the collision, then re-inspect the postings' effective account.
```

## G04-L10N_TH-Q009

```yaml
QID: G04-L10N_TH-Q009
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  After installation, a user must be able to determine which accounts originated from the localisation and which existed before it, without relying on memory.
WHY_IT_MATTERS: >
  Without this distinction, a reviewer cannot separate the localisation's own structure from customer customization when auditing the chart.
DISCONFIRMING_OBSERVATION: >
  There is no available indicator, listing, or attribute that distinguishes localisation-origin accounts from pre-existing ones after installation.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Install the localisation onto a database with pre-existing custom accounts, then attempt to enumerate which accounts came from the localisation.
```

## G04-L10N_TH-Q010

```yaml
QID: G04-L10N_TH-Q010
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A single accounting entry must resolve to exactly one branch or head-office attribution, never more than one at the same time.
WHY_IT_MATTERS: >
  An entry attributed to more than one unit simultaneously would make branch-level reporting double-count or misattribute results.
DISCONFIRMING_OBSERVATION: >
  A single entry's stored attribution or its reporting inclusion shows more than one branch/head-office unit at once.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Post an entry in a context where more than one branch attribution is technically available, then inspect its resolved attribution.
```

## G04-L10N_TH-Q011

```yaml
QID: G04-L10N_TH-Q011
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Whether each branch maintains its own independent document-numbering series or shares one with head office is a configurable choice, not a fixed behaviour.
WHY_IT_MATTERS: >
  A fixed behaviour would prevent adapting numbering to how branches are actually structured for a given customer.
DISCONFIRMING_OBSERVATION: >
  No configuration path changes whether a branch shares or has its own series; the behaviour is the same regardless of settings tried.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Attempt to configure independent versus shared numbering series for two branches and observe whether the resulting document numbers actually change behaviour.
```

## G04-L10N_TH-Q012

```yaml
QID: G04-L10N_TH-Q012
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An entry that lacks an explicit branch attribution must be blocked from posting or must receive an attribution through an explicit, visible default rule, not an untraceable one.
WHY_IT_MATTERS: >
  An untraceable default can misattribute results without anyone able to explain why.
DISCONFIRMING_OBSERVATION: >
  An entry posts with a branch attribution that cannot be traced to either an explicit user choice or a documented default rule.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Attempt to post an entry without specifying branch attribution and inspect what attribution, if any, results and why.
```

## G04-L10N_TH-Q013

```yaml
QID: G04-L10N_TH-Q013
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  The mapping between a generic document type and the localised document type the localisation introduces remains adjustable after installation, not frozen at install time.
WHY_IT_MATTERS: >
  A frozen mapping would prevent correcting a wrong initial mapping without reinstalling.
DISCONFIRMING_OBSERVATION: >
  No supported path exists to change the mapping between a generic document type and its localised counterpart after installation.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Install the localisation, then attempt to change the mapping between a generic document type and the localised type it was mapped to.
```

## G04-L10N_TH-Q014

```yaml
QID: G04-L10N_TH-Q014
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When a document is cancelled before finalization, the numbering-gap behaviour (reuse versus permanent gap) is applied consistently across every document type the localisation adds.
WHY_IT_MATTERS: >
  Inconsistent gap behaviour across document types would make the numbering trail unreliable to interpret.
DISCONFIRMING_OBSERVATION: >
  Two different localisation-added document types handle the same cancellation-before-finalization scenario differently (one reuses the number, another leaves a gap) with no documented reason.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel a document before finalization for each localisation-added document type and compare the resulting numbering behaviour.
```

## G04-L10N_TH-Q015

```yaml
QID: G04-L10N_TH-Q015
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Two documents created at effectively the same time under the same branch series must each receive a distinct number, with no duplicate assigned.
WHY_IT_MATTERS: >
  A duplicate number would break the uniqueness the numbering series exists to guarantee.
DISCONFIRMING_OBSERVATION: >
  Two concurrently created documents under the same series end up with the same number, or the series silently skips more numbers than its own gap policy allows.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger near-simultaneous creation of two documents under the same branch series and inspect the numbers assigned to each.
```

## G04-L10N_TH-Q016

```yaml
QID: G04-L10N_TH-Q016
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A number reserved but never used because the transaction failed to commit leaves a gap that is distinguishable, in the audit trail, from a gap caused by an intentional cancellation.
WHY_IT_MATTERS: >
  Conflating the two gap causes would prevent a reviewer from telling a technical failure apart from a business cancellation.
DISCONFIRMING_OBSERVATION: >
  The audit trail shows the same evidence, or no evidence, for a failure-caused gap as for a cancellation-caused gap.
EXPECTED_SURFACE: S6,S8
PRECONDITIONS: >
  Force a transaction to fail after a number is reserved but before commit, then compare the resulting trail to that of a normal cancellation.
```

## G04-L10N_TH-Q017

```yaml
QID: G04-L10N_TH-Q017
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When a tax configuration change carries a future effective date, a document is subject to the statutory rate configured as in force on that document's tax point date, not the rate in force on the date the configuration was changed.
WHY_IT_MATTERS: >
  Applying the wrong effective rate misstates the tax basis of the transaction relative to when it is deemed to have occurred.
DISCONFIRMING_OBSERVATION: >
  A document whose tax point date falls before the new configuration's effective date is computed using the new rate, or vice versa.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Schedule a tax configuration change with a future effective date, then create documents with tax point dates on either side of that date and inspect the rate applied to each.
LEGAL_TAX_REVIEW_REQUIRED: YES
```
## G04-L10N_TH-Q018

```yaml
QID: G04-L10N_TH-Q018
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a tax rule is applied retroactively rather than effective-dated, the system's actual scope of recomputation (already-posted documents, or only new documents) is explicit and does not silently include documents the operator did not intend to touch.
WHY_IT_MATTERS: >
  An unintended silent recomputation of posted documents would misstate figures already reported without anyone choosing that outcome.
DISCONFIRMING_OBSERVATION: >
  Applying a retroactive tax rule change measurably alters the stored tax amount of a document that was already posted, with no explicit action or record showing that document was intended to be included.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Apply a tax rule marked as retroactive rather than effective-dated, then check whether already-posted documents' stored tax amounts changed.
LEGAL_TAX_REVIEW_REQUIRED: YES
```

## G04-L10N_TH-Q019

```yaml
QID: G04-L10N_TH-Q019
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The statutory rate configured as in force is selected using the transaction's tax point date, consistently, even when the posting date or document date differ from it.
WHY_IT_MATTERS: >
  Using the wrong date to select the rate would apply a rate that was never actually in force for that transaction.
DISCONFIRMING_OBSERVATION: >
  Two documents with the same tax point date but different posting or document dates end up computed with different rates, or a document's rate follows its posting date rather than its tax point date.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create documents where document date, posting date, and tax point date are deliberately set apart, spanning a rate change, and inspect which date determined the rate used.
LEGAL_TAX_REVIEW_REQUIRED: YES
```

## G04-L10N_TH-Q020

```yaml
QID: G04-L10N_TH-Q020
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Editing the membership of a reporting grouping the localisation defines must not retroactively change the figures of a report already generated before the edit.
WHY_IT_MATTERS: >
  A retroactively changing historical report would make it impossible to know what was actually reported at the time.
DISCONFIRMING_OBSERVATION: >
  Regenerating a previously generated report after a grouping-membership edit produces different totals for the same historical period without any indication that the underlying grouping changed.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Generate and retain a report, edit the membership of a reporting grouping it uses, then regenerate the same historical report and compare.
```

## G04-L10N_TH-Q021

```yaml
QID: G04-L10N_TH-Q021
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A reporting grouping's definition at any past point in time can be reconstructed, not only its current definition.
WHY_IT_MATTERS: >
  Without reconstructable history, a reviewer cannot verify how a past report's totals were actually derived.
DISCONFIRMING_OBSERVATION: >
  After a grouping's membership has been edited more than once, there is no way to determine what its membership was at an earlier point in time.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Edit a reporting grouping's membership more than once over time, then attempt to determine its membership as of an earlier date.
```

## G04-L10N_TH-Q022

```yaml
QID: G04-L10N_TH-Q022
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A change to a reporting grouping applies to new activity going forward; a document already classified under the prior grouping keeps that original classification in its own stored record.
WHY_IT_MATTERS: >
  If a document's own stored classification silently follows the current grouping definition instead of the one at the time, its history becomes unstable.
DISCONFIRMING_OBSERVATION: >
  A document created before a grouping change shows a different grouping classification, in its own stored record, after the change than it showed before.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create a document under one grouping definition, change the grouping's definition, then re-inspect the original document's stored classification.
```

## G04-L10N_TH-Q023

```yaml
QID: G04-L10N_TH-Q023
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Reprinting a document reproduces the content and layout that were in force at the moment the document was originally issued, not the configuration in force at the moment of reprinting.
WHY_IT_MATTERS: >
  A reprint that silently reflects current configuration would not be a true copy of what was actually issued.
DISCONFIRMING_OBSERVATION: >
  Reprinting a document after a relevant configuration change (layout, tax display, or numbering rule) produces content that differs from the original issuance in ways not present in the original.
EXPECTED_SURFACE: S1,S5,S7
PRECONDITIONS: >
  Issue a document, change the relevant configuration, then reprint the same document and compare it against a retained copy of the original.
```

## G04-L10N_TH-Q024

```yaml
QID: G04-L10N_TH-Q024
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A reprint of a previously issued document is distinguishable, in the system trail, from an original issuance of that same document.
WHY_IT_MATTERS: >
  An indistinguishable reprint would let someone present a reissued copy as if it were the first and only original.
DISCONFIRMING_OBSERVATION: >
  The system trail, or the reprinted output itself, provides no way to tell that a given output is a reprint rather than the original issuance.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Issue a document, then reprint it, and inspect both the output and the system trail for any distinguishing marker.
```

## G04-L10N_TH-Q025

```yaml
QID: G04-L10N_TH-Q025
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  The language used for printed and exported output is a configurable choice at an appropriate level (company, branch, or document), not hard-fixed regardless of setting.
WHY_IT_MATTERS: >
  A fixed language would prevent serving the audiences that actually need the local-language document.
DISCONFIRMING_OBSERVATION: >
  Changing the relevant language configuration has no effect on the language actually produced on a printed or exported document.
EXPECTED_SURFACE: S5,S7
PRECONDITIONS: >
  Change the configured output language at the appropriate level and generate the same document before and after to compare the language actually produced.
```

## G04-L10N_TH-Q026

```yaml
QID: G04-L10N_TH-Q026
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  The value stored for a data element that appears on a printed or exported document matches, without alteration, what is actually rendered on that output.
WHY_IT_MATTERS: >
  A drift between stored and rendered value would mean the printed document does not accurately represent the system's own record.
DISCONFIRMING_OBSERVATION: >
  A value rendered on a printed or exported document differs from the corresponding value held in the stored record, beyond an explicitly documented formatting transformation.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Compare a data element's stored value against its rendering on a printed and on an exported version of the same document.
```

## G04-L10N_TH-Q027

```yaml
QID: G04-L10N_TH-Q027
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An exported version of a document, made available to a different party for electronic exchange, shows the same substantive values as the printed copy the original recipient received.
WHY_IT_MATTERS: >
  A divergence would mean two parties are relying on two different versions of what is supposed to be the same document.
DISCONFIRMING_OBSERVATION: >
  The exported version of a document contains a substantive value (amount, date, party identifier) that differs from the printed copy of the same document.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Generate both the printed and the exported form of the same document and compare their substantive content.
```

## G04-L10N_TH-Q028

```yaml
QID: G04-L10N_TH-Q028
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Where rounding is applied at the line level, the sum of rounded lines is reconciled against the document-level total, and any residual difference is explicitly recorded rather than silently absorbed into an unrelated line.
WHY_IT_MATTERS: >
  A silently absorbed residual would misstate the line it landed on for a reason unrelated to that line's actual content.
DISCONFIRMING_OBSERVATION: >
  The document total does not equal the sum of its rounded lines, with no separately recorded residual explaining the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Construct a document whose line amounts round unevenly, then inspect how the total is derived from the rounded lines.
```

## G04-L10N_TH-Q029

```yaml
QID: G04-L10N_TH-Q029
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Where the localisation's tax-rounding convention differs from the platform's general rounding convention, the localisation's convention takes effect for locally taxed amounts, and which convention was applied is visible.
WHY_IT_MATTERS: >
  An unnoticed use of the wrong rounding convention would produce a tax figure inconsistent with the statutory rounding basis configured for the jurisdiction.
DISCONFIRMING_OBSERVATION: >
  A locally taxed amount is rounded using the platform's general convention rather than the locally configured one, with no indication of which convention was actually applied.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure a local tax-rounding convention that differs from the platform default, compute a tax amount that would round differently under each, and inspect which result and which convention marker appears.
LEGAL_TAX_REVIEW_REQUIRED: YES
```

## G04-L10N_TH-Q030

```yaml
QID: G04-L10N_TH-Q030
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A residual amount arising from rounding is recorded in a way that is distinguishable, in the audit trail, from a deliberate manual adjustment entry.
WHY_IT_MATTERS: >
  Conflating the two would let a rounding residual mask, or be mistaken for, an intentional adjustment.
DISCONFIRMING_OBSERVATION: >
  A rounding residual and a deliberate manual adjustment of the same size are recorded identically, with no way to tell them apart in the trail.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Produce a document with a rounding residual and, separately, a manual adjustment of the same amount, then compare their recorded trail.
```

## G04-L10N_TH-Q031

```yaml
QID: G04-L10N_TH-Q031
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  The localisation's behaviour (chart entries, tax setup, document requirements) applies only within the scope of the company it targets, and does not become the default behaviour for a second company in another jurisdiction sharing the same database.
WHY_IT_MATTERS: >
  Leakage into an unrelated jurisdiction's company would apply a locally specific rule where it has no legal basis.
DISCONFIRMING_OBSERVATION: >
  A company in a different jurisdiction, sharing the same database, exhibits a chart entry, tax computation, or document requirement introduced by the localisation without it being explicitly assigned to that company.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Install the localisation for one company in a database that also holds a second company in a different jurisdiction, then inspect the second company's chart, tax setup, and document behaviour.
```

## G04-L10N_TH-Q032

```yaml
QID: G04-L10N_TH-Q032
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A report consolidating both companies applies the localisation-specific reporting grouping only to the applicable company's data, and clearly marks it as not applicable to the other company's data rather than leaving it blank or defaulted.
WHY_IT_MATTERS: >
  An unmarked absence could be misread as the other company having zero activity in that grouping, rather than the grouping not applying to it.
DISCONFIRMING_OBSERVATION: >
  A consolidated report shows the other company's data under a localisation-specific grouping, or shows a value with no indication that the grouping does not apply to that company.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Generate a consolidated report spanning both companies and inspect how the localisation-specific grouping is represented for each.
```

## G04-L10N_TH-Q033

```yaml
QID: G04-L10N_TH-Q033
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  A transaction against a legacy master record that lacks data the localisation requires is blocked with a specific reason, rather than proceeding under a silent assumed default.
WHY_IT_MATTERS: >
  A silent default could produce a locally required document or tax treatment the record's actual data does not support.
DISCONFIRMING_OBSERVATION: >
  A transaction against a master record missing the newly required data posts successfully with no indication that a default was assumed in place of missing data.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Identify a legacy master record lacking data the localisation requires, then attempt a transaction against it.
```

## G04-L10N_TH-Q034

```yaml
QID: G04-L10N_TH-Q034
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  After installation, there is a way to identify every existing master record missing data the localisation now requires, rather than the gap only surfacing one record at a time as each is transacted against.
WHY_IT_MATTERS: >
  Discovering gaps only at transaction time delays remediation and risks inconsistent handling across records.
DISCONFIRMING_OBSERVATION: >
  No listing, report, or check exists that identifies, in one pass, all master records missing the newly required data after installation.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Install the localisation onto a database containing legacy master records with varying completeness, then look for a way to identify all records missing the newly required data.
```
## G04-L10N_TH-Q035

```yaml
QID: G04-L10N_TH-Q035
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Given a document produced under the localisation, a reviewer can establish which localisation version and which configuration state were in effect when it was produced.
WHY_IT_MATTERS: >
  Without this, a reviewer cannot explain why a given document looks the way it does relative to current configuration.
DISCONFIRMING_OBSERVATION: >
  There is no stored or derivable record linking a produced document to the localisation version and configuration state that were in effect at the time it was produced.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Produce a document under one localisation version and configuration state, change both, then attempt to determine which version and state produced the original document.
```

## G04-L10N_TH-Q036

```yaml
QID: G04-L10N_TH-Q036
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  When the localisation is updated between a document's issuance and a later audit, the configuration state that was in effect at issuance remains available to the audit, not overwritten without trace.
WHY_IT_MATTERS: >
  An overwritten configuration history would make it impossible to reconstruct why a past document looks as it does.
DISCONFIRMING_OBSERVATION: >
  After an update, no record of the prior configuration state remains available, even though documents produced under it still exist.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Issue a document, update the localisation, then attempt to retrieve the configuration state that was in effect when the document was issued.
```

## G04-L10N_TH-Q037

```yaml
QID: G04-L10N_TH-Q037
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Approving a locally required document type advances its approval status only; it does not, by itself, perform the accounting posting of the underlying transaction.
WHY_IT_MATTERS: >
  If approval silently posts, the approval-execution-posting separation the programme requires is violated for this jurisdiction's document types too.
DISCONFIRMING_OBSERVATION: >
  A locally required document type becomes posted as a direct and immediate consequence of an approval action, with no distinct posting step or event.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Approve a locally required document type that is not yet posted, and observe whether posting occurs as part of the same action or requires a separate step.
```

## G04-L10N_TH-Q038

```yaml
QID: G04-L10N_TH-Q038
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Revoking or reversing an approval on a locally required document type does not, by itself, unpost a transaction that was already posted; unposting requires its own distinct action.
WHY_IT_MATTERS: >
  Coupling the two would let an approval-level action silently undo a financial posting without going through the posting-reversal path.
DISCONFIRMING_OBSERVATION: >
  Reversing an approval on an already-posted, locally required document results in that document becoming unposted with no separate, distinct unposting action recorded.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Approve and post a locally required document, then revoke the approval and observe whether the posting itself is affected.
```

## G04-L10N_TH-Q039

```yaml
QID: G04-L10N_TH-Q039
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  The role permitted to post or unpost a locally required document type is distinct from, and not automatically granted by, the role permitted to edit its configuration.
WHY_IT_MATTERS: >
  Conflating the two roles would let someone who can only configure the localisation also control live postings.
DISCONFIRMING_OBSERVATION: >
  A user who holds only the configuration-edit role, without an explicit posting role, is able to post or unpost a locally required document.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Grant a user only the configuration-edit role for the localisation and attempt to post or unpost a document as that user.
```

## G04-L10N_TH-Q040

```yaml
QID: G04-L10N_TH-Q040
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A document that was posted and later unposted (or its local equivalent voided) is distinguishable, in the trail, from a document that was never posted at all.
WHY_IT_MATTERS: >
  An indistinguishable state would erase the evidence that a posting ever happened and was reversed.
DISCONFIRMING_OBSERVATION: >
  An unposted document's trail or current state is identical to that of a document that was never posted, with no evidence remaining that posting occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Post a document, then unpost it, and compare its resulting state and trail to a document that was never posted.
```

## G04-L10N_TH-Q041

```yaml
QID: G04-L10N_TH-Q041
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling a posted, locally required document retains the document's original number and content in a visible, marked-cancelled state, rather than removing it.
WHY_IT_MATTERS: >
  Removal would create a numbering gap indistinguishable from other causes and destroy the evidence of what was cancelled and why.
DISCONFIRMING_OBSERVATION: >
  A cancelled document is no longer retrievable in any form, or is retrievable without any indication that it was cancelled versus still active.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Post a locally required document, cancel it, then attempt to retrieve it and inspect its state.
```

## G04-L10N_TH-Q042

```yaml
QID: G04-L10N_TH-Q042
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When a locally required document is reversed, whether the system restores the original state or records a new compensating entry is consistent and is visibly distinguishable in the trail, not ambiguous.
WHY_IT_MATTERS: >
  Ambiguity between the two would prevent a reviewer from correctly interpreting the net effect of the reversal on the books.
DISCONFIRMING_OBSERVATION: >
  Reversing the same type of document twice under the same circumstances produces different mechanisms (once a restore, once a new entry), or the trail does not indicate which mechanism occurred.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Reverse a locally required document and inspect whether the original entry is restored or a new compensating entry is created, and how the trail represents it.
```

## G04-L10N_TH-Q043

```yaml
QID: G04-L10N_TH-Q043
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where a tax rule is defined generically, outside the localisation, and also covered by the localisation's own local tax setup, which one takes precedence is explicit and consistent, not silently arbitrary.
WHY_IT_MATTERS: >
  An arbitrary or inconsistent precedence would make the effective tax treatment unpredictable for the same configuration.
DISCONFIRMING_OBSERVATION: >
  The same combination of a generically defined rule and a locally defined rule produces different effective tax treatment on different occasions with no configuration change between them.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure both a generically defined tax rule and a locally defined one that could both apply to the same transaction, and observe which one takes effect, repeated more than once.
```

## G04-L10N_TH-Q044

```yaml
QID: G04-L10N_TH-Q044
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  If a locally required document type is optional and later disabled, documents already created under that requirement remain intact and retrievable rather than becoming invalid or disappearing.
WHY_IT_MATTERS: >
  Silently invalidating existing documents when a requirement is toggled off would destroy previously valid records for no substantive reason.
DISCONFIRMING_OBSERVATION: >
  Disabling an optional local document requirement causes existing documents created under it to become inaccessible, invalid, or altered.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Enable an optional local document requirement, create documents under it, disable the requirement, then attempt to retrieve those documents.
```

## G04-L10N_TH-Q045

```yaml
QID: G04-L10N_TH-Q045
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Every configuration item the localisation requires to be set is exposed through some user-accessible path, not left as an internal default with no way for a user to change it.
WHY_IT_MATTERS: >
  A required item with no accessible path would leave a customer unable to correct it if the default is wrong for their situation.
DISCONFIRMING_OBSERVATION: >
  A configuration item the localisation depends on for correct behaviour has no user-accessible way to view or change its value.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Identify a configuration item the localisation's behaviour depends on and attempt to locate a user-accessible path to view and change it.
```

## G04-L10N_TH-Q046

```yaml
QID: G04-L10N_TH-Q046
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Every locally defined document type or tax rule that appears available in configuration can actually be reached and used through a normal transaction flow.
WHY_IT_MATTERS: >
  A configured-but-unreachable item would mislead a user into believing a capability exists when it cannot actually be used.
DISCONFIRMING_OBSERVATION: >
  A locally defined document type or tax rule is selectable or visible in configuration but cannot actually be produced or applied through any normal transaction flow.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Enumerate the locally defined document types and tax rules exposed in configuration, then attempt to actually use each one in a normal transaction flow.
```

## G04-L10N_TH-Q047

```yaml
QID: G04-L10N_TH-Q047
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  The numbering rule or tax rule as declared in configuration matches what is actually produced when a transaction is run end-to-end, without divergence.
WHY_IT_MATTERS: >
  A divergence between declared configuration and actual runtime behaviour would make the configuration screen an unreliable description of the system.
DISCONFIRMING_OBSERVATION: >
  Running a transaction end-to-end produces a number or tax result that does not match what the declared configuration specifies.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Record the declared numbering and tax configuration, run a transaction end-to-end, and compare the actual result against the declared configuration.
```

## G04-L10N_TH-Q048

```yaml
QID: G04-L10N_TH-Q048
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A transaction missing a locally required reference is rejected before it posts, rather than being allowed to post and only flagged afterward.
WHY_IT_MATTERS: >
  Allowing it to post first would let a non-compliant transaction enter the books before the deficiency is caught.
DISCONFIRMING_OBSERVATION: >
  A transaction missing a locally required reference successfully posts, with the deficiency only surfaced by a later check.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Attempt to post a transaction deliberately missing a locally required reference and observe at what point, if any, it is rejected.
```

## G04-L10N_TH-Q049

```yaml
QID: G04-L10N_TH-Q049
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  The total of locally required documents issued for a period can be reconciled against the corresponding accounting entries for that period using the system's own available data, without a manual side calculation outside it.
WHY_IT_MATTERS: >
  If reconciliation requires an external manual calculation, discrepancies are more likely to go undetected.
DISCONFIRMING_OBSERVATION: >
  No available report or query within the system allows comparing the total of locally required documents for a period against the corresponding accounting entries without exporting data for a manual calculation.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Attempt to reconcile the total of locally required documents for a period against the accounting entries for that period using only what the system itself provides.
```

## G04-L10N_TH-Q050

```yaml
QID: G04-L10N_TH-Q050
MODULE: l10n_th
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A locally required document passes through distinguishable lifecycle states (such as draft, issued, cancelled), with each transition individually logged rather than the document collapsing straight from draft to a final state with no intermediate record.
WHY_IT_MATTERS: >
  Collapsed transitions would erase the ability to know when and by whom each stage actually occurred.
DISCONFIRMING_OBSERVATION: >
  A locally required document's trail shows only its final state, with no record of the intermediate transitions it must have passed through.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Move a locally required document through its full lifecycle and inspect the trail for a distinct, timestamped record of each transition.
```
