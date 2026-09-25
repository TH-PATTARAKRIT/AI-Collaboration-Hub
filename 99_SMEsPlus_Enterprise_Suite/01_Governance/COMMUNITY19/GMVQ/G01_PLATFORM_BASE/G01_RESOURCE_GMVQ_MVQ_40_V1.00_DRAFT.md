# SMEsPlus ENTERPRISE SUITE
## GMVQ - G01 PLATFORM_BASE / resource Module Adversarial MVQ Bank

**Document ID:** GMVQ-G01-RESOURCE-MVQ40-V1.00  
**Group:** G01 PLATFORM_BASE  
**Module Metadata:** `resource`  
**Destination:** SAAS_FOUNDATION  
**Status:** AUTHORING COMPLETE / QA COMPLETE / W1-B12 FROZEN  
**Lane A / Lane B:** NOT EXECUTED HERE

## Control
QUESTION_BANK_STANDARD_55_V2.00 is reused unchanged. These 40 module-specific questions are behavioral and source-neutral. Every record includes DISCONFIRMING_OBSERVATION, risk tier, evidence surface and precondition. Counts are Question Programme tracking only and are not Formal Coverage.

## G01-RESOURCE-Q001

```yaml
QID: G01-RESOURCE-Q001
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: "Creating a resource for a company without an explicit working calendar selects that company's governed default calendar."
WHY_IT_MATTERS: "A resource must not silently inherit scheduling rules from another company."
DISCONFIRMING_OBSERVATION: "A newly created company-specific resource receives a calendar belonging to a different company or an unrelated default."
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: "Create resources in two companies while omitting an explicit calendar."
```

## G01-RESOURCE-Q002

```yaml
QID: G01-RESOURCE-Q002
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: CONSTRAINT
HYPOTHESIS: "A resource cannot retain a working calendar that violates the governed company boundary."
WHY_IT_MATTERS: "Cross-company calendars can corrupt availability and capacity planning."
DISCONFIRMING_OBSERVATION: "Changing or importing a resource leaves it linked to a calendar outside the allowed company scope."
EXPECTED_SURFACE: S1,S4,S5,S6
PRECONDITIONS: "Attempt UI and import/API assignments of calendars from another company."
```

## G01-RESOURCE-Q003

```yaml
QID: G01-RESOURCE-Q003
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: "Changing a resource's company recomputes or requires an explicit valid working calendar for the new company."
WHY_IT_MATTERS: "Company changes must not leave stale scheduling configuration."
DISCONFIRMING_OBSERVATION: "After changing company, the resource keeps the old company's calendar without a blocking rule or explicit exception."
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: "Create a resource with a company calendar, then change company."
```

## G01-RESOURCE-Q004

```yaml
QID: G01-RESOURCE-Q004
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: "Linking a user to a human resource aligns the resource timezone with the governed user timezone when no explicit contrary rule applies."
WHY_IT_MATTERS: "Scheduling must interpret the same person's working time consistently."
DISCONFIRMING_OBSERVATION: "Linking a user leaves a stale timezone that changes computed working periods."
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: "Link users with distinct timezones to otherwise equivalent resources."
```

## G01-RESOURCE-Q005

```yaml
QID: G01-RESOURCE-Q005
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: "A resource timezone change shifts presentation and calculation boundaries without changing the underlying absolute interval incorrectly."
WHY_IT_MATTERS: "Timezone conversion must not create or lose working time."
DISCONFIRMING_OBSERVATION: "The same absolute period gains, loses, or duplicates working hours solely because it is viewed under another timezone."
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: "Compare identical UTC intervals under two resource timezones including a DST boundary where applicable."
```

## G01-RESOURCE-Q006

```yaml
QID: G01-RESOURCE-Q006
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: "Archiving a resource hides it from normal active use without deleting its historical identity."
WHY_IT_MATTERS: "Operational deactivation must preserve traceability."
DISCONFIRMING_OBSERVATION: "Archiving deletes the resource, breaks historical references, or leaves it selectable as an active resource without explicit override."
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: "Archive a resource already referenced by a downstream record."
```

## G01-RESOURCE-Q007

```yaml
QID: G01-RESOURCE-Q007
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: "Human and material resource types remain behaviorally distinguishable wherever downstream scheduling relies on resource type."
WHY_IT_MATTERS: "Type is a business classification, not cosmetic metadata."
DISCONFIRMING_OBSERVATION: "A material resource is treated as a linked human user, or a human resource loses user-related semantics without an explicit rule."
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: "Create equivalent human and material resources and compare supported scheduling flows."
```

## G01-RESOURCE-Q008

```yaml
QID: G01-RESOURCE-Q008
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: CONSTRAINT
HYPOTHESIS: "Resource efficiency must be strictly positive."
WHY_IT_MATTERS: "Zero or negative efficiency makes duration calculations undefined or inverted."
DISCONFIRMING_OBSERVATION: "A resource can persist an efficiency factor of zero or less."
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: "Attempt create and update with zero and negative efficiency values."
```

## G01-RESOURCE-Q009

```yaml
QID: G01-RESOURCE-Q009
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: "An efficiency factor of 100 percent preserves the baseline expected duration."
WHY_IT_MATTERS: "The neutral efficiency point must not distort planning."
DISCONFIRMING_OBSERVATION: "A one-hour baseline operation yields a different expected duration at 100 percent efficiency."
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: "Compare a known baseline duration at 100 percent efficiency."
```

## G01-RESOURCE-Q010

```yaml
QID: G01-RESOURCE-Q010
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: "Efficiency above 100 percent shortens expected duration proportionally under the governed calculation."
WHY_IT_MATTERS: "Capacity planning depends on monotonic efficiency behavior."
DISCONFIRMING_OBSERVATION: "Increasing efficiency above 100 percent increases or leaves unchanged the expected duration when the factor is applicable."
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: "Compare the same operation at 100 and 200 percent efficiency."
```

## G01-RESOURCE-Q011

```yaml
QID: G01-RESOURCE-Q011
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: "Efficiency below 100 percent but above zero lengthens expected duration proportionally under the governed calculation."
WHY_IT_MATTERS: "Slower resources must not appear faster in plans."
DISCONFIRMING_OBSERVATION: "Reducing efficiency below 100 percent shortens the expected duration."
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: "Compare the same operation at 100 and 50 percent efficiency."
```

## G01-RESOURCE-Q012

```yaml
QID: G01-RESOURCE-Q012
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: "A resource with no working calendar is treated as fully flexible only under the explicit flexible-resource rule."
WHY_IT_MATTERS: "Absence of configuration must have deterministic semantics."
DISCONFIRMING_OBSERVATION: "A calendar-less resource is inconsistently treated as unavailable in one supported calculation and fully available in another."
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: "Run availability and work-interval calculations for a resource with no calendar."
```

## G01-RESOURCE-Q013

```yaml
QID: G01-RESOURCE-Q013
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: "A resource assigned to a calendar marked flexible follows the flexible-calendar rule consistently across supported work-time calculations."
WHY_IT_MATTERS: "Flexible schedules must not oscillate between fixed and flexible semantics."
DISCONFIRMING_OBSERVATION: "One work-time API treats the calendar as flexible while another enforces fixed attendance periods for the same interval."
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: "Compare work-day and interval calculations on a flexible calendar."
```

## G01-RESOURCE-Q014

```yaml
QID: G01-RESOURCE-Q014
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: "When a resource has no explicit calendar but a governed company default exists, supported calculations use the documented fallback consistently."
WHY_IT_MATTERS: "Fallback behavior must be predictable across services."
DISCONFIRMING_OBSERVATION: "Different scheduling operations choose different fallback calendars for the same resource."
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: "Remove the explicit resource calendar and exercise multiple work-time operations."
```

## G01-RESOURCE-Q015

```yaml
QID: G01-RESOURCE-Q015
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: "Adjusting a start datetime to a calendar returns the nearest governed effective working start within the applicable day or an explicit no-match result."
WHY_IT_MATTERS: "Boundary adjustment drives scheduling accuracy."
DISCONFIRMING_OBSERVATION: "A start outside attendance is moved to a non-working instant or silently crosses the governed day without rule."
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: "Use starts before, inside, between and after attendance periods."
```

## G01-RESOURCE-Q016

```yaml
QID: G01-RESOURCE-Q016
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: "Adjusting an end datetime to a calendar returns the nearest governed effective working end within the applicable rule or an explicit no-match result."
WHY_IT_MATTERS: "End boundaries must not create phantom work."
DISCONFIRMING_OBSERVATION: "An end outside attendance is adjusted to a time that adds non-working duration."
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: "Use ends before, inside, between and after attendance periods."
```

## G01-RESOURCE-Q017

```yaml
QID: G01-RESOURCE-Q017
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: "When leave computation is enabled, applicable time off removes overlapping work intervals for the affected resource."
WHY_IT_MATTERS: "Availability must honor governed unavailability."
DISCONFIRMING_OBSERVATION: "A resource remains fully available during an overlapping leave when leave computation is enabled."
EXPECTED_SURFACE: S1,S4,S5,S6
PRECONDITIONS: "Create an overlapping resource leave and compute work intervals with leaves enabled."
```

## G01-RESOURCE-Q018

```yaml
QID: G01-RESOURCE-Q018
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: "When a supported calculation explicitly disables leave computation, attendance is evaluated without subtracting leave while all other calendar rules remain intact."
WHY_IT_MATTERS: "The compute-leaves switch must have one precise effect."
DISCONFIRMING_OBSERVATION: "Disabling leave computation still subtracts leave or changes unrelated attendance boundaries."
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: "Compare the same interval with leave computation enabled and disabled."
```

## G01-RESOURCE-Q019

```yaml
QID: G01-RESOURCE-Q019
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: "A resource-specific leave affects only the targeted resource unless an explicit shared rule applies."
WHY_IT_MATTERS: "One resource's absence must not remove capacity from unrelated resources."
DISCONFIRMING_OBSERVATION: "A leave tied to resource A removes working time from resource B on the same calendar."
EXPECTED_SURFACE: S1,S4,S5,S6
PRECONDITIONS: "Use two resources on one calendar and create leave for only one."
```

## G01-RESOURCE-Q020

```yaml
QID: G01-RESOURCE-Q020
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: "A generic calendar-level leave applies to the governed scope of resources using that calendar."
WHY_IT_MATTERS: "Shared closures must affect all intended resources consistently."
DISCONFIRMING_OBSERVATION: "A calendar closure affects only an arbitrary subset of resources sharing that calendar."
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: "Create a calendar-wide closure and compare multiple resources on that calendar."
```

## G01-RESOURCE-Q021

```yaml
QID: G01-RESOURCE-Q021
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: CONSTRAINT
HYPOTHESIS: "A time-off interval cannot persist with a start later than its end."
WHY_IT_MATTERS: "Inverted intervals corrupt availability calculations."
DISCONFIRMING_OBSERVATION: "Create or update accepts date_from greater than date_to."
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: "Attempt direct create, edit and import/API write with inverted dates."
```

## G01-RESOURCE-Q022

```yaml
QID: G01-RESOURCE-Q022
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: "Default full-day time-off boundaries are derived using the applicable calendar or user timezone and stored without shifting to an unintended local date."
WHY_IT_MATTERS: "Default values must preserve the intended calendar day."
DISCONFIRMING_OBSERVATION: "Opening a default leave in a non-UTC timezone produces a stored interval covering the prior or next local date."
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: "Create default leave records under several timezones."
```

## G01-RESOURCE-Q023

```yaml
QID: G01-RESOURCE-Q023
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: "Time-off classification distinguishes unavailable leave from other time classifications according to the governed domain used by work calculations."
WHY_IT_MATTERS: "Classification controls whether time is removed from capacity."
DISCONFIRMING_OBSERVATION: "An entry classified outside the leave domain is still subtracted as leave without an explicit rule, or a leave entry is ignored."
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: "Create otherwise identical entries with different time classifications."
```

## G01-RESOURCE-Q024

```yaml
QID: G01-RESOURCE-Q024
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONSTRAINT
HYPOTHESIS: "Attendance hour boundaries cannot remain below zero or above the governed end-of-day limit after normal user editing."
WHY_IT_MATTERS: "Out-of-range hours create impossible schedules."
DISCONFIRMING_OBSERVATION: "An attendance persists with negative start, start above the daily bound, or end beyond the daily bound through a normal supported edit."
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: "Enter boundary and out-of-range attendance hours through supported UI flows."
```

## G01-RESOURCE-Q025

```yaml
QID: G01-RESOURCE-Q025
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: CONSTRAINT
HYPOTHESIS: "An attendance period cannot end before it starts."
WHY_IT_MATTERS: "Negative attendance duration must be prevented."
DISCONFIRMING_OBSERVATION: "A period with end earlier than start is accepted and contributes negative or inverted working time."
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: "Attempt start/end combinations in reverse order."
```

## G01-RESOURCE-Q026

```yaml
QID: G01-RESOURCE-Q026
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: "A designated lunch or break attendance contributes no working duration unless an explicit configuration says otherwise."
WHY_IT_MATTERS: "Breaks must not inflate capacity."
DISCONFIRMING_OBSERVATION: "A lunch or break line increases calculated work hours."
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: "Add a lunch or break line inside an otherwise fixed workday."
```

## G01-RESOURCE-Q027

```yaml
QID: G01-RESOURCE-Q027
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONSTRAINT
HYPOTHESIS: "A duration-based calendar rejects a break attendance configuration that conflicts with its duration semantics."
WHY_IT_MATTERS: "Duration-based schedules require internally consistent attendance records."
DISCONFIRMING_OBSERVATION: "A break attendance is accepted in duration-based mode even though it creates contradictory duration accounting."
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: "Enable duration-based behavior and attempt to persist a lunch or break attendance."
```

## G01-RESOURCE-Q028

```yaml
QID: G01-RESOURCE-Q028
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: "Changing attendance duration through a supported inverse edit updates the corresponding time boundaries deterministically for full-day, morning and afternoon periods."
WHY_IT_MATTERS: "Duration editing must not produce ambiguous times."
DISCONFIRMING_OBSERVATION: "Equivalent duration edits produce different start/end boundaries for the same day-period type."
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: "Edit duration for full-day, morning and afternoon attendance records."
```

## G01-RESOURCE-Q029

```yaml
QID: G01-RESOURCE-Q029
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: "Alternating-week attendance parity remains continuous across year boundaries, including years with an extra numbered week."
WHY_IT_MATTERS: "Two-week schedules must not repeat or skip the wrong logical week at New Year."
DISCONFIRMING_OBSERVATION: "The first/second week sequence produces two consecutive logical weeks of the same parity because of calendar week numbering."
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: "Test alternating-week schedules across multiple year-end boundaries."
```

## G01-RESOURCE-Q030

```yaml
QID: G01-RESOURCE-Q030
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: "Copying an attendance preserves its governed scheduling attributes without copying unrelated transient state."
WHY_IT_MATTERS: "Schedule duplication must be predictable."
DISCONFIRMING_OBSERVATION: "A copied attendance loses day, hour, period, week type, display section or sequence values required to reproduce the schedule."
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: "Duplicate representative fixed and alternating-week attendance lines."
```

## G01-RESOURCE-Q031

```yaml
QID: G01-RESOURCE-Q031
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: "Copying a resource creates a distinct resource identity while preserving applicable company, calendar and timezone configuration unless explicitly overridden."
WHY_IT_MATTERS: "A copy must not alias the original resource."
DISCONFIRMING_OBSERVATION: "The duplicate shares the same identity or unexpectedly changes scheduling configuration without an override."
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: "Copy a configured resource and compare identity and scheduling fields."
```

## G01-RESOURCE-Q032

```yaml
QID: G01-RESOURCE-Q032
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: "Creating a record that uses the resource mixin without an explicit resource creates exactly one backing resource with aligned identity, company, calendar and timezone."
WHY_IT_MATTERS: "Bridge models must not create orphan or duplicate resources."
DISCONFIRMING_OBSERVATION: "Creation produces no backing resource, multiple resources, or a resource with mismatched company, calendar or timezone."
EXPECTED_SURFACE: S1,S4,S5,S6
PRECONDITIONS: "Create mixin-based records with and without explicit company, calendar and timezone values."
```

## G01-RESOURCE-Q033

```yaml
QID: G01-RESOURCE-Q033
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: "Copying a record that owns a backing resource creates an independent backing resource rather than sharing mutable scheduling identity with the original."
WHY_IT_MATTERS: "Copied business objects must not unintentionally share resource state."
DISCONFIRMING_OBSERVATION: "Changing calendar or timezone on the copy also changes the original because both point to the same resource."
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: "Copy a mixin-based record and modify scheduling fields on the copy."
```

## G01-RESOURCE-Q034

```yaml
QID: G01-RESOURCE-Q034
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: "Writable company and calendar values exposed through a resource-backed record remain synchronized with the backing resource and cannot diverge into contradictory states."
WHY_IT_MATTERS: "Related scheduling fields must represent one identity."
DISCONFIRMING_OBSERVATION: "The business record shows company or calendar values that differ from its backing resource after a supported write."
EXPECTED_SURFACE: S1,S4,S5,S6
PRECONDITIONS: "Write company and calendar through both supported record surfaces and compare resulting state."
```

## G01-RESOURCE-Q035

```yaml
QID: G01-RESOURCE-Q035
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: "Batch work-day calculation returns days and hours derived from the same effective intervals for each resource."
WHY_IT_MATTERS: "Summary metrics must reconcile to interval evidence."
DISCONFIRMING_OBSERVATION: "Reported work days or hours cannot be reconstructed from effective attendance and leave intervals for the same resource."
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: "Compare batch work-day output with interval-level calculations for multiple calendars."
```

## G01-RESOURCE-Q036

```yaml
QID: G01-RESOURCE-Q036
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: "Work and leave calculations for fully flexible resources follow one explicit rule rather than mixing fixed-calendar assumptions into the result."
WHY_IT_MATTERS: "Flexible resources otherwise produce misleading capacity numbers."
DISCONFIRMING_OBSERVATION: "A fully flexible resource yields contradictory hours across work-day, leave-day and interval operations for the same period without a documented rule."
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: "Exercise work and leave calculations for a calendar-less resource."
```

## G01-RESOURCE-Q037

```yaml
QID: G01-RESOURCE-Q037
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: "Per-day work-time listing assigns hours to the correct local day for the governed timezone."
WHY_IT_MATTERS: "Daily totals feed planning and reporting boundaries."
DISCONFIRMING_OBSERVATION: "An overnight or timezone-shifted interval is attributed to the wrong local date or counted twice."
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: "Use timezone-aware intervals near midnight and compare daily aggregation."
```

## G01-RESOURCE-Q038

```yaml
QID: G01-RESOURCE-Q038
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: "Listed leave time is limited to the intersection of applicable leave and working attendance for the resource."
WHY_IT_MATTERS: "Leave outside scheduled work must not inflate lost capacity."
DISCONFIRMING_OBSERVATION: "A leave entirely outside attendance contributes positive working leave hours."
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: "Create leave both inside and outside attendance and compare listed leave hours."
```

## G01-RESOURCE-Q039

```yaml
QID: G01-RESOURCE-Q039
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: "Batch calculations isolate resources by their applicable calendars and do not cross-apply one resource's intervals to another."
WHY_IT_MATTERS: "Grouped execution must preserve record identity."
DISCONFIRMING_OBSERVATION: "Two resources on different calendars receive identical or swapped interval results because of batching."
EXPECTED_SURFACE: S1,S4,S5,S6
PRECONDITIONS: "Calculate a batch containing resources with deliberately different calendars and timezones."
```

## G01-RESOURCE-Q040

```yaml
QID: G01-RESOURCE-Q040
MODULE: resource
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: "Resource, calendar and leave data from one unrelated SaaS customer boundary cannot alter or become visible in another customer's governed scheduling context."
WHY_IT_MATTERS: "Resource scheduling is security-sensitive shared infrastructure."
DISCONFIRMING_OBSERVATION: "A resource, calendar, leave, or computed availability from customer A is readable or applied in unrelated customer B without an explicit shared-governance rule."
EXPECTED_SURFACE: S1,S4,S5,S6
PRECONDITIONS: "Use two unrelated customer boundaries with similar resource names and schedules."
```

