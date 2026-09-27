# SMEsPlus ENTERPRISE SUITE
## GMVQ — G03 MASTER_DATA / product Module MVQ Bank

**Document ID:** GMVQ-G03-PRODUCT-MVQ48-V1.00
**Group:** G03 MASTER_DATA
**Module Metadata:** `product`
**Wave:** W1
**Author Cell:** TEAM 17 (Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose

This bank supplies the module-specific MVQ set for `product`, the master item record: variants, attributes, units, categories, pricing, and the accounts attached to it and to its category. Per the G03 MASTER_DATA group brief, this is a top-risk master record because it carries income, expense and valuation account attribution, and its category carries stock valuation, so the questions reach that accounting rather than stopping at the form. Coverage is spread across business capability, business rule, state transition, configuration dependency, role and permission, exception path, cancellation, reversal, negative case, cross-module dependency, optional behaviour, auditability, tenant/company boundary, concurrency and ordering, runtime reachability, configuration reachability, and source/runtime contradiction potential. This bank supplements the 35-question Standard bank; combined research depth for this module is 35 + 48 = 83.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure state, never a restatement of its own hypothesis.
- No padding: 48 questions exist because they test 48 distinct material hypotheses; none was trimmed or stretched to hit the count.
- Question text is source-neutral: no vendor or product name, no technical identifier (table, field, method, XML ID, API path), and the module's own metadata name never appears outside the `MODULE:` field — the generic term "item record" stands in for it throughout.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready. Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G03-PRODUCT-Q001

```yaml
QID: G03-PRODUCT-Q001
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Changing the income or expense account attributed to an item record after transactions on that record have already been posted must not restate the accounting of those already-posted transactions.
WHY_IT_MATTERS: >
  Silent restatement of closed financial periods would misstate previously reported results and break audit trust in posted history.
DISCONFIRMING_OBSERVATION: >
  A previously posted transaction's ledger entries change value, account, or amount purely because the item record's account attribution was edited afterward, with no explicit correcting or reversing action taken.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post at least one transaction referencing an item record with a known account attribution, then change that attribution and inspect the original posted entries.
```

## G03-PRODUCT-Q002

```yaml
QID: G03-PRODUCT-Q002
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Changing the stock valuation account attributed to an item record after inventory movements have been posted against it must not retroactively alter the value already recorded for those movements.
WHY_IT_MATTERS: >
  Retroactive valuation drift would break the reconciliation between recorded inventory value and financial statements already issued.
DISCONFIRMING_OBSERVATION: >
  The recorded value of an already-posted stock movement changes after the valuation account attribution is edited, without a distinct correcting movement being created.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post a stock movement for an item record with a known valuation account, then change that attribution and compare the movement's recorded value before and after.
```

## G03-PRODUCT-Q003

```yaml
QID: G03-PRODUCT-Q003
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When an item record and the category it belongs to both carry an explicit account attribution for the same purpose and they disagree, exactly one of the two takes effect according to a documented, consistent precedence rule.
WHY_IT_MATTERS: >
  An undocumented or inconsistent precedence rule between two conflicting sources of accounting truth produces unpredictable postings that are difficult to diagnose.
DISCONFIRMING_OBSERVATION: >
  A transaction posts using the record's own attribution in one case and the category's attribution in an otherwise-equivalent case, with no configuration difference explaining the switch.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Set differing account attributions on an item record and on its category for the same purpose, then post a transaction and identify which value was actually used.
```

## G03-PRODUCT-Q004

```yaml
QID: G03-PRODUCT-Q004
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When an item record has no explicit account attribution of its own, the value inherited from its category is used consistently across every transaction type that requires that attribution.
WHY_IT_MATTERS: >
  Inconsistent fallback behaviour across transaction types would mean some postings silently use no account at all or an unintended default.
DISCONFIRMING_OBSERVATION: >
  Two different transaction types referencing the same item record with no attribution of its own resolve to two different accounts, or one of them fails to resolve at all.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Clear the item record's own account attribution, leave only the category's set, and post more than one transaction type referencing the record.
```

## G03-PRODUCT-Q005

```yaml
QID: G03-PRODUCT-Q005
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An item record shared across more than one company can carry a distinct account attribution per company, and each company's transactions use only that company's attribution.
WHY_IT_MATTERS: >
  A single shared attribution across companies would leak one company's chart of accounts structure into another company's books.
DISCONFIRMING_OBSERVATION: >
  A transaction posted under one company uses an account attribution that was configured for a different company on the same shared item record.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Share one item record across two companies, set different account attributions per company where supported, and post a transaction under each company.
```

## G03-PRODUCT-Q006

```yaml
QID: G03-PRODUCT-Q006
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When a company sharing an item record has not configured its own account attribution, the system resolves a defined company-scoped default rather than silently borrowing another company's configured value.
WHY_IT_MATTERS: >
  Borrowing another company's value would be a cross-company data leak disguised as a convenience default.
DISCONFIRMING_OBSERVATION: >
  A company with no attribution of its own posts using an account value that was configured specifically for a different company, not a value defined at the company's own level.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure an account attribution for company A only on a shared item record, then post a transaction for company B referencing the same record.
```

## G03-PRODUCT-Q007

```yaml
QID: G03-PRODUCT-Q007
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Creating a new variant on an item record that already has movement history on other variants does not itself carry forward that unrelated movement history.
WHY_IT_MATTERS: >
  A new variant inheriting another variant's movement history would fabricate inventory or financial history that never occurred for it.
DISCONFIRMING_OBSERVATION: >
  A newly created variant shows opening quantity, cost, or movement history that originated from a sibling variant rather than from its own transactions.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create movement history on one variant of an item record, then create a new sibling variant and inspect its starting state.
```

## G03-PRODUCT-Q008

```yaml
QID: G03-PRODUCT-Q008
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A variant that already has recorded movement cannot be archived or deactivated in a way that silently removes it from historical reports while still permitting new documents to reference it.
WHY_IT_MATTERS: >
  A variant that is invisible in reporting but still selectable would let new transactions accumulate against effectively untracked inventory.
DISCONFIRMING_OBSERVATION: >
  A variant with movement history disappears from historical valuation or quantity reports after being archived, yet remains selectable for a new document.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Create movement history on a variant, archive or deactivate it, then check both historical reporting and new-document selection.
```

## G03-PRODUCT-Q009

```yaml
QID: G03-PRODUCT-Q009
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A variant that already has recorded movement cannot be permanently deleted; deletion is blocked or redirected to archiving rather than removing the record entirely.
WHY_IT_MATTERS: >
  Permanently deleting a record with financial movement destroys the audit trail those movements depend on for reconciliation.
DISCONFIRMING_OBSERVATION: >
  A variant with existing movement history is permanently deleted and its referencing movements remain, now pointing at a record that no longer exists.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Create movement history on a variant, then attempt to permanently delete that variant through every path available.
```

## G03-PRODUCT-Q010

```yaml
QID: G03-PRODUCT-Q010
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Switching an item record's tracking basis (for example enabling lot or serial tracking) after transactions already exist does not retroactively assign tracking identity to those pre-existing transactions.
WHY_IT_MATTERS: >
  Retroactively fabricating lot or serial identity for historical transactions would create traceability records that misrepresent what was actually tracked at the time.
DISCONFIRMING_OBSERVATION: >
  Transactions that existed before tracking was enabled show a lot, serial, or equivalent identity value that could not have been captured at the time they were recorded.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Post transactions against an item record with no tracking basis, enable a tracking basis afterward, and inspect the pre-existing transactions for newly appeared tracking data.
```

## G03-PRODUCT-Q011

```yaml
QID: G03-PRODUCT-Q011
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Switching an item record's costing method after transactions already exist does not silently recompute and overwrite the valuation already recorded for those prior transactions.
WHY_IT_MATTERS: >
  Silent recomputation under a new costing method would change previously reported financial results without an auditable correcting entry.
DISCONFIRMING_OBSERVATION: >
  The recorded value of a transaction that predates a costing method change is different after the change than it was before, with no explicit correcting entry created.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post transactions under one costing method, switch the item record to a different costing method, and compare the pre-existing transactions' recorded values before and after.
```

## G03-PRODUCT-Q012

```yaml
QID: G03-PRODUCT-Q012
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Changing an item record's unit of measure after on-hand stock exists either blocks the change or performs an explicit, auditable conversion of the existing quantity and value rather than reinterpreting the stored number under the new unit.
WHY_IT_MATTERS: >
  Reinterpreting a stored quantity under a new, incompatible unit silently multiplies or divides the true on-hand value without anyone intending it.
DISCONFIRMING_OBSERVATION: >
  After the unit of measure is changed, the on-hand quantity or value figure is read as if measured in the new unit without any recorded conversion step.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Establish on-hand stock for an item record under one unit of measure, then change its unit of measure and inspect the resulting on-hand figures and any conversion record.
```

## G03-PRODUCT-Q013

```yaml
QID: G03-PRODUCT-Q013
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Changing an item record's unit-of-measure category after stock or transactions exist, where the old and new categories are not compatibly convertible, is blocked rather than allowed to proceed with an undefined conversion.
WHY_IT_MATTERS: >
  An undefined conversion between incompatible measurement categories produces a meaningless quantity that can propagate into shipping, billing, and valuation.
DISCONFIRMING_OBSERVATION: >
  The unit-of-measure category is changed to an incompatible one while stock exists, and the system proceeds without blocking or without a defined conversion outcome.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Establish stock under one unit-of-measure category, then attempt to change the item record to a unit-of-measure category with no defined conversion to the original.
```

## G03-PRODUCT-Q014

```yaml
QID: G03-PRODUCT-Q014
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An item record marked as a service rather than a stocked good is prevented from accumulating stock quantity or valuation entries through any document path.
WHY_IT_MATTERS: >
  A service silently accumulating inventory valuation would corrupt both the service's own reporting and any inventory valuation reports that aggregate across records.
DISCONFIRMING_OBSERVATION: >
  A document path produces a stock quantity or valuation entry against an item record that is configured as a service rather than a stocked good.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure an item record as a service, then attempt every document path that would normally create a stock movement for a stocked good.
```

## G03-PRODUCT-Q015

```yaml
QID: G03-PRODUCT-Q015
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Converting an item record from a stocked type to a service type (or the reverse) while open stock quantity exists is blocked, or the existing stock is explicitly resolved as part of the conversion.
WHY_IT_MATTERS: >
  Open stock left stranded by a silent type conversion would be neither trackable as inventory nor accounted as a service, disappearing from both views.
DISCONFIRMING_OBSERVATION: >
  An item record's type is changed while it holds open stock quantity, and afterward that quantity is neither visible in stock reporting nor accounted for anywhere else.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Establish open stock quantity on a stocked item record, then attempt to change its type to a service and inspect where the prior stock quantity ends up.
```

## G03-PRODUCT-Q016

```yaml
QID: G03-PRODUCT-Q016
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The figure used for customer-facing pricing, the figure used for internal cost, and the figure recorded as inventory valuation are three independently maintained numbers, and editing one does not silently overwrite another.
WHY_IT_MATTERS: >
  Collapsing three distinct financial concepts into one editable number would make margin analysis and valuation both unreliable.
DISCONFIRMING_OBSERVATION: >
  Editing the customer-facing price, or the internal cost figure, changes the recorded inventory valuation figure (or vice versa) without an explicit action intended to do so.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record distinct values for price, cost, and valuation on an item record, then edit one of the three and inspect whether the other two remain unchanged.
```

## G03-PRODUCT-Q017

```yaml
QID: G03-PRODUCT-Q017
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A manually edited cost figure on an item record persists until a defined recomputation event occurs, rather than being silently overwritten by a background recomputation at an undocumented time.
WHY_IT_MATTERS: >
  An unpredictable silent overwrite of a manually corrected cost figure would erase a deliberate correction without any indication to the person who made it.
DISCONFIRMING_OBSERVATION: >
  A manually edited cost value reverts to a system-computed value without any transaction, recomputation trigger, or notice that would explain the change.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Manually edit the cost figure on an item record under an automated costing method, then observe the value over time and across any background processing cycle.
```

## G03-PRODUCT-Q018

```yaml
QID: G03-PRODUCT-Q018
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A change to an item record's account attribution that can alter a future financial outcome is captured in an audit trail identifying what changed, from what value, to what value, by whom, and when.
WHY_IT_MATTERS: >
  Without a captured trail, a financially consequential master-data change is indistinguishable from data that was always that way, defeating any later investigation.
DISCONFIRMING_OBSERVATION: >
  An account attribution on an item record is changed and no trace of the prior value, the new value, the actor, or the time is retrievable afterward.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change an account attribution on an item record and attempt to retrieve a complete before/after/actor/time record of that change.
```

## G03-PRODUCT-Q019

```yaml
QID: G03-PRODUCT-Q019
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Archiving or deactivating an item record that is still referenced by an open, unconfirmed document either blocks the archiving or clearly flags the open reference rather than silently allowing both to proceed unrelated to each other.
WHY_IT_MATTERS: >
  A silently archived record still sitting on an open document can be confirmed later without anyone noticing it points at something no longer active.
DISCONFIRMING_OBSERVATION: >
  An item record referenced by an open, unconfirmed document is archived with no warning, and the open document later confirms successfully as if nothing changed.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create an open, unconfirmed document referencing an item record, then archive that item record and attempt to confirm the document.
```

## G03-PRODUCT-Q020

```yaml
QID: G03-PRODUCT-Q020
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Archiving an item record that is referenced only by closed, historical documents does not remove or degrade the readability of those historical documents.
WHY_IT_MATTERS: >
  Historical records becoming unreadable after routine archiving would damage the ability to answer audit questions about closed periods.
DISCONFIRMING_OBSERVATION: >
  A closed historical document referencing an archived item record becomes unreadable, incomplete, or shows an error where the item's details used to appear.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Close a document referencing an item record, archive that item record, and reopen the closed document to inspect how the reference renders.
```

## G03-PRODUCT-Q021

```yaml
QID: G03-PRODUCT-Q021
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An item record scoped to one tenant cannot be referenced, selected, or read by a document or user operating under a different tenant.
WHY_IT_MATTERS: >
  Cross-tenant visibility of master data is a fundamental breach of the isolation a multi-tenant platform promises its customers.
DISCONFIRMING_OBSERVATION: >
  A document or search operating under one tenant returns, selects, or reads an item record that belongs to a different tenant.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create item records under two distinct tenants with distinguishable names, then attempt to reference or search for one from within the other tenant's context.
```

## G03-PRODUCT-Q022

```yaml
QID: G03-PRODUCT-Q022
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An item record scoped to one company within a tenant, and not explicitly shared, cannot be selected on a document created under a different company in the same tenant.
WHY_IT_MATTERS: >
  Unintended cross-company selection would let one legal entity's transactions reference another entity's private master data.
DISCONFIRMING_OBSERVATION: >
  A document created under company B successfully references an item record scoped to company A with no explicit sharing configured between them.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Scope an item record to company A only, then attempt to select it on a new document created under company B.
```

## G03-PRODUCT-Q023

```yaml
QID: G03-PRODUCT-Q023
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A user role that can edit an item record's basic descriptive information but has not been granted accounting configuration rights cannot change its account attribution through any available path.
WHY_IT_MATTERS: >
  A permission boundary that only blocks the obvious path but not an adjacent one is a broken boundary, not a real one.
DISCONFIRMING_OBSERVATION: >
  A user without accounting configuration rights successfully changes an item record's account attribution through an editing path intended for basic descriptive fields.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Assign a role with basic edit rights but no accounting configuration rights, and attempt to change the item record's account attribution through every editing surface available to that role.
```

## G03-PRODUCT-Q024

```yaml
QID: G03-PRODUCT-Q024
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The right to view an item record's internal cost figure and the right to view its recorded valuation figure are separately controllable, not bundled under a single permission.
WHY_IT_MATTERS: >
  Bundling two distinct sensitive figures under one permission forces an over-broad grant whenever only one of them is actually needed.
DISCONFIRMING_OBSERVATION: >
  A role granted visibility into one of the two figures (cost or valuation) automatically gains visibility into the other with no separate grant.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Grant a role visibility into only one of the cost or valuation figures and check whether the other becomes visible as a side effect.
```

## G03-PRODUCT-Q025

```yaml
QID: G03-PRODUCT-Q025
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Attempting to attribute an account to an item record or its category that is of a type incompatible with that category's valuation configuration is rejected rather than accepted and left to fail later at posting time.
WHY_IT_MATTERS: >
  Deferring an incompatible configuration error to posting time turns a preventable configuration mistake into a transaction-time failure that blocks real business activity.
DISCONFIRMING_OBSERVATION: >
  An incompatible account type is accepted at the point of attribution with no warning, and the incompatibility only surfaces later when a transaction attempts to post.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to attribute an account of a type known to be incompatible with the category's valuation configuration, and observe whether the system rejects it immediately.
```

## G03-PRODUCT-Q026

```yaml
QID: G03-PRODUCT-Q026
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A change to a category's valuation configuration has a defined, documented effect on item records already assigned to that category — either applying immediately to all of them or applying only to records created afterward — and that effect is consistent across records.
WHY_IT_MATTERS: >
  An inconsistent or undefined cascade means some existing records under the category silently use stale valuation behaviour while others do not.
DISCONFIRMING_OBSERVATION: >
  Two item records under the same category, both existing before the category's valuation configuration changed, behave differently from each other after the change with no distinguishing configuration between them.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Assign two item records to the same category, change the category's valuation configuration, and compare both records' subsequent behaviour.
```

## G03-PRODUCT-Q027

```yaml
QID: G03-PRODUCT-Q027
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reversing a document that referenced an item record whose account attribution has since changed uses the account attribution that was in effect at the time of the original transaction, not the currently configured one.
WHY_IT_MATTERS: >
  A reversal posting to a different account than the original transaction breaks the pairing that reconciliation and audit depend on.
DISCONFIRMING_OBSERVATION: >
  A reversal of an original transaction posts to an account different from the one the original transaction used, solely because the item record's attribution changed in between.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post a transaction referencing an item record, change that record's account attribution, then reverse the original transaction and compare the accounts used.
```

## G03-PRODUCT-Q028

```yaml
QID: G03-PRODUCT-Q028
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Re-confirming a previously cancelled draft document whose referenced item record's category changed in the interim re-derives accounting attribution from the current configuration in a way that is explicit and visible, not silently mismatched against what was shown when the draft was first created.
WHY_IT_MATTERS: >
  A silent mismatch between what a draft displayed and what it actually posts under would mean the person confirming it approves numbers they never saw.
DISCONFIRMING_OBSERVATION: >
  A draft document confirms using account attribution different from what was displayed on the draft, with no re-display or confirmation of the new values before posting.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a draft document referencing an item record, change the record's category configuration, then confirm the draft and compare displayed versus posted attribution.
```

## G03-PRODUCT-Q029

```yaml
QID: G03-PRODUCT-Q029
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Creating an item record with no explicit accounting attribution of its own and no resolvable fallback from its category either blocks creation, blocks the record from being used in a posting transaction, or clearly flags it as incomplete — it does not silently default to an arbitrary account.
WHY_IT_MATTERS: >
  An arbitrary silent default for a financially significant attribute produces incorrect postings with no configuration decision behind them.
DISCONFIRMING_OBSERVATION: >
  An item record with no attribution of its own and no category fallback is used in a posted transaction that resolves to some account with no configuration having specified it.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create an item record and its category with no accounting attribution configured on either, then attempt to post a transaction referencing that record.
```

## G03-PRODUCT-Q030

```yaml
QID: G03-PRODUCT-Q030
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two concurrent edits to the same shared item record's account attribution from two different sessions are resolved deterministically — either the later write is clearly the one that takes effect, or a conflict is surfaced — rather than producing an inconsistent or partially applied result.
WHY_IT_MATTERS: >
  An undetected conflict between concurrent edits to a financially significant attribute can leave the record in a state nobody intended and nobody can explain.
DISCONFIRMING_OBSERVATION: >
  After two concurrent edits from different sessions, the item record's attribution reflects a value that matches neither edit, or the two sessions each believe their own edit is the one in effect.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Open the same item record for editing in two separate sessions, change its account attribution differently in each, and save both.
```

## G03-PRODUCT-Q031

```yaml
QID: G03-PRODUCT-Q031
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A bulk or mass-update path for changing account attribution across many item records at once enforces the same validation rules as editing a single record individually.
WHY_IT_MATTERS: >
  A bulk path that skips single-record validation is a systematic way to introduce invalid or incompatible attributions across many records at once.
DISCONFIRMING_OBSERVATION: >
  A bulk update accepts an account attribution value that the single-record edit path would have rejected.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Identify an attribution value rejected by single-record editing, then attempt to apply that same value through a bulk or mass-update path.
```

## G03-PRODUCT-Q032

```yaml
QID: G03-PRODUCT-Q032
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Enabling multi-currency or multi-company configuration at the tenant level changes which fields become mandatory on an item record in a way that is applied consistently to records created both before and after the configuration change.
WHY_IT_MATTERS: >
  Inconsistent mandatory-field enforcement between old and new records under the same configuration would leave some records permanently incomplete relative to current rules.
DISCONFIRMING_OBSERVATION: >
  An item record created before a multi-currency or multi-company configuration change remains permanently exempt from a field that is mandatory for every record created after, with no path to bring it into compliance.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create an item record before enabling multi-currency or multi-company configuration, enable the configuration, then compare mandatory-field enforcement between the old and a newly created record.
```

## G03-PRODUCT-Q033

```yaml
QID: G03-PRODUCT-Q033
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Any administrative path that allows overriding the normal category-versus-record precedence for accounting attribution on a per-record basis is itself restricted to a distinct, auditable permission rather than reachable by the same role that manages ordinary record edits.
WHY_IT_MATTERS: >
  An unguarded override of the precedence rule would let an ordinary editor quietly bypass a control meant to be an explicit exception.
DISCONFIRMING_OBSERVATION: >
  A role with only ordinary record-edit rights can invoke a precedence override without any distinct permission check or audit trace.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Locate any override path for the category-versus-record precedence rule and check what permission and audit trace it requires.
```

## G03-PRODUCT-Q034

```yaml
QID: G03-PRODUCT-Q034
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Moving an item record from an inactive or draft state into an active, usable state does not itself trigger a retroactive accounting validation or posting against transactions that occurred, or were prepared, while it was inactive.
WHY_IT_MATTERS: >
  A retroactive validation triggered purely by a state change could post or alter transactions based on data that was never meant to be final.
DISCONFIRMING_OBSERVATION: >
  Activating a previously inactive item record causes a posting or valuation change to occur immediately, without any transaction being newly created or confirmed.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create an item record in an inactive state with some prepared but unconfirmed data, then activate it and observe whether any posting occurs without a separate confirming action.
```

## G03-PRODUCT-Q035

```yaml
QID: G03-PRODUCT-Q035
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Rounding applied to the customer-facing price and rounding applied to the internal cost figure are governed independently, so the two can legitimately diverge without one silently constraining the other.
WHY_IT_MATTERS: >
  If cost rounding silently inherits price rounding precision (or the reverse), margin calculations built on both figures become subtly wrong.
DISCONFIRMING_OBSERVATION: >
  Changing the rounding precision configured for price also changes the stored precision or displayed value of the cost figure, or vice versa, with no configuration link intended between them.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Configure distinct rounding precision for price and for cost on an item record, change one, and check whether the other is affected.
```

## G03-PRODUCT-Q036

```yaml
QID: G03-PRODUCT-Q036
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A report reading the current recorded valuation of an item record whose account attribution changed partway through its life reconciles fully with the sum of the individual ledger entries that were posted under each attribution in effect at the time.
WHY_IT_MATTERS: >
  A valuation report that no longer reconciles with the underlying ledger entries after a mid-life attribution change would be silently wrong in a way that is hard to detect until an audit.
DISCONFIRMING_OBSERVATION: >
  The current valuation reported for an item record does not equal the sum of its individual posted ledger entries once account attribution has changed partway through its transaction history.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post transactions before and after changing an item record's account attribution, then compare the current valuation report against the sum of the underlying ledger entries.
```

## G03-PRODUCT-Q037

```yaml
QID: G03-PRODUCT-Q037
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a variant carries its own account attribution different from the shared template it belongs to, the variant's own attribution takes precedence for that variant's transactions, consistently.
WHY_IT_MATTERS: >
  An inconsistent precedence between a variant's own attribution and its shared template would mean some of a variant's transactions post correctly and others silently revert to the template's setting.
DISCONFIRMING_OBSERVATION: >
  A transaction against a variant with its own account attribution posts using the shared template's attribution instead, or the choice varies unpredictably between otherwise-equivalent transactions.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Set a variant's own account attribution different from its shared template's, then post more than one transaction type against that variant.
```

## G03-PRODUCT-Q038

```yaml
QID: G03-PRODUCT-Q038
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two item records that appear to represent the same real-world good but carry different accounting attributions are flagged or detectable as likely duplicates before any operation would merge or consolidate their histories.
WHY_IT_MATTERS: >
  A silent merge of two records with different accounting attributions would blend two different financial treatments into one history with no way to tell which figures came from which source.
DISCONFIRMING_OBSERVATION: >
  Two near-identical item records with differing accounting attributions can be merged or consolidated with no warning about the attribution mismatch.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create two item records with matching descriptive detail but different accounting attributions, and attempt any available merge or consolidation path between them.
```

## G03-PRODUCT-Q039

```yaml
QID: G03-PRODUCT-Q039
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Archiving a category that still has item records assigned to it either blocks the archiving or leaves those records with a clearly resolved effective account attribution, rather than an unresolved one.
WHY_IT_MATTERS: >
  Item records left with an unresolved attribution after their category disappears could fail postings unpredictably or default to something no one chose.
DISCONFIRMING_OBSERVATION: >
  A category with assigned item records is archived, and afterward at least one of those records has no resolvable account attribution for a required posting.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Assign item records to a category that itself carries the fallback attribution, archive that category, and attempt a posting transaction against one of the assigned records.
```

## G03-PRODUCT-Q040

```yaml
QID: G03-PRODUCT-Q040
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The recorded valuation figure for an item record cannot go negative through ordinary transaction processing without an explicit, distinguishable exception path being taken.
WHY_IT_MATTERS: >
  An unexplained negative valuation figure usually signals either a data error or an unrecorded business event, and silently allowing it hides which one occurred.
DISCONFIRMING_OBSERVATION: >
  An item record's valuation figure goes negative through ordinary transaction processing with no distinct flag, warning, or exception record associated with it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Drive an item record's recorded quantity or value toward zero and below through ordinary transactions and observe what happens as it crosses zero.
```

## G03-PRODUCT-Q041

```yaml
QID: G03-PRODUCT-Q041
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A bulk import or export path for item records enforces the same mandatory accounting attribution requirements as manual single-record creation.
WHY_IT_MATTERS: >
  A bulk path that bypasses mandatory accounting fields is a systematic way to introduce financially incomplete master data at volume.
DISCONFIRMING_OBSERVATION: >
  A bulk import creates item records lacking a mandatory account attribution that manual single-record creation would have required.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Identify an accounting attribution mandatory for manual creation, then attempt a bulk import of item records omitting that attribution.
```

## G03-PRODUCT-Q042

```yaml
QID: G03-PRODUCT-Q042
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Customer-facing pricing that is shared globally across companies and any pricing that is scoped per company are clearly distinguished, so a company-scoped price never silently overwrites the shared global value seen by other companies.
WHY_IT_MATTERS: >
  A company-scoped price bleeding into the shared global value would let one company's negotiated pricing surface to every other company sharing the record.
DISCONFIRMING_OBSERVATION: >
  A price set for one company on a shared item record is also reflected as the value seen by a different company that has not configured its own price.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Share an item record across two companies, set a distinct price scoped to one company, and check what price the other company sees.
```

## G03-PRODUCT-Q043

```yaml
QID: G03-PRODUCT-Q043
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the account referenced by an item record's attribution is itself later archived or disabled, any attempt to post a new transaction against that record is blocked or clearly flagged rather than posting to a disabled account.
WHY_IT_MATTERS: >
  Posting to a disabled account produces a transaction that financial reporting may exclude or mishandle without anyone realizing the underlying account was no longer active.
DISCONFIRMING_OBSERVATION: >
  A new transaction posts successfully to an account that has been archived or disabled since it was attributed to the item record.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Attribute an account to an item record, archive or disable that account, and attempt to post a new transaction referencing the record.
```

## G03-PRODUCT-Q044

```yaml
QID: G03-PRODUCT-Q044
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A manual change to an item record's cost figure and a change produced by an automated background recomputation are distinguishable from each other in whatever audit trail records the change.
WHY_IT_MATTERS: >
  An audit trail that cannot tell a deliberate manual correction apart from an automated recompute makes it impossible to investigate why a cost figure is wrong.
DISCONFIRMING_OBSERVATION: >
  Two cost-figure changes with different actual origins — one manual, one from a background process — appear identical or indistinguishable in the audit trail.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Trigger one manual cost edit and one background recomputation on comparable item records, then compare how each appears in the audit trail.
```

## G03-PRODUCT-Q045

```yaml
QID: G03-PRODUCT-Q045
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A scheduled background recomputation of an average or standard cost figure and a concurrent manual edit to the same figure resolve deterministically, with a documented outcome for which one takes effect, rather than an unpredictable race.
WHY_IT_MATTERS: >
  An unpredictable race between a scheduled job and a manual edit means the same sequence of actions can produce different final figures on different days.
DISCONFIRMING_OBSERVATION: >
  Repeating the same manual edit timed against the same background recomputation window produces a different final cost figure on different occasions with no other variable changed.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Time a manual cost edit to occur during a scheduled recomputation window for the same item record, and repeat the scenario to check for consistency.
```

## G03-PRODUCT-Q046

```yaml
QID: G03-PRODUCT-Q046
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Marking an item record as discontinued or end-of-life blocks its use on new documents while leaving existing draft documents that already reference it able to be completed or explicitly rejected, rather than left in an undefined state.
WHY_IT_MATTERS: >
  A discontinued record leaving in-flight drafts in an undefined state creates work that can neither be finished nor cleanly cancelled.
DISCONFIRMING_OBSERVATION: >
  An existing draft document referencing a newly discontinued item record can neither be completed nor explicitly cancelled, and provides no indication of why.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create a draft document referencing an item record, mark that record discontinued, and attempt to complete or cancel the draft.
```

## G03-PRODUCT-Q047

```yaml
QID: G03-PRODUCT-Q047
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Rounding differences introduced by unit conversion on individual document lines do not accumulate silently across many lines of the same document into a materially different total than the sum of the unrounded values would produce.
WHY_IT_MATTERS: >
  Silent accumulation of small rounding differences across a large document can produce a total that no longer reconciles with a line-by-line recalculation.
DISCONFIRMING_OBSERVATION: >
  The total of a document with many unit-converted lines differs materially from the sum of each line's individually calculated, unrounded value, beyond what a single line's rounding could explain.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Build a document with many lines referencing an item record that requires unit conversion, and compare the document total against an independent line-by-line recalculation.
```

## G03-PRODUCT-Q048

```yaml
QID: G03-PRODUCT-Q048
MODULE: product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Changing an item record's fundamental type — for example converting it from a service to a stocked good — after it already has both sales and purchase history is blocked, or is accompanied by an explicit resolution of what that prior history now means.
WHY_IT_MATTERS: >
  A silent type conversion over existing history leaves historical transactions describing a kind of record that no longer matches what the record now is.
DISCONFIRMING_OBSERVATION: >
  An item record's fundamental type changes while sales and purchase history already exist against it, and the historical documents display or behave as if that history always matched the new type.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Build sales and purchase history against an item record of one fundamental type, then attempt to convert its type and inspect how the prior history is displayed afterward.
```
