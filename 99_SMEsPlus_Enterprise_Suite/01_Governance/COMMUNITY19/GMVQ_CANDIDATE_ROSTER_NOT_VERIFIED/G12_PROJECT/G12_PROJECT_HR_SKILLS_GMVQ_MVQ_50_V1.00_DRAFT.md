# SMEsPlus ENTERPRISE SUITE
## GMVQ — G12 PROJECT / project_hr_skills Module MVQ Bank

**Document ID:** GMVQ-G12-PROJECT_HR_SKILLS-MVQ50-V1.00
**Group:** G12 PROJECT (Wave 3)
**Module Metadata:** `project_hr_skills`
**Module Class:** Foundation (treated at normal/full scope per Group G12 brief and control-desk
routing note, notwithstanding its two-domain name) — not restricted to seam-only questions
**Wave:** W3
**Author Cell:** P12-2 (GMVQ Question Factory — Production Cell P12-2)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies the module-specific (MVQ) tier for skill-based project staffing: how a required
competency for a task or project is matched against employee skill records, how that match is
computed, surfaced, overridden, audited, and kept consistent as skill data and staffing needs change
over time. This module carries two layers — the skill catalog and an employee's recorded skill data
(BASE), and the matching/assignment behaviour that consumes it for staffing (PROCESS) — tagged
accordingly per the Authoring Standard.

Question text is source-neutral. It does not name the module, any vendor or product, or any
technical identifier (field, model, method, XML ID, API path).

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: 50 questions exist because each tests a distinct material hypothesis, spread across
  business rule, state transition, configuration dependency, role and permission, exception path,
  reversal, negative case, cross-module dependency, auditability, tenant/company boundary, and
  concurrency.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only. No Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not MASTER-ready.

## G12-PROJECT_HR_SKILLS-Q001

```yaml
QID: G12-PROJECT_HR_SKILLS-Q001
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When a task requires a specific skill, the staffing suggestion surfaces only employees who actually
  hold that skill as candidates, rather than the full team indiscriminately.
WHY_IT_MATTERS: >
  A suggestion list that ignores the stated requirement provides no real filtering value and forces
  every decision back onto manual judgment.
DISCONFIRMING_OBSERVATION: >
  A staffing suggestion for a task requiring a specific skill includes employees who do not hold that
  skill, with no distinction from those who do.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Define a task requiring a specific skill held by only some team members and request a staffing
  suggestion.
```

## G12-PROJECT_HR_SKILLS-Q002

```yaml
QID: G12-PROJECT_HR_SKILLS-Q002
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Skill proficiency level, not merely presence or absence of the skill, is considered when suggesting
  a candidate for a task, rather than treating every holder of the skill as equally suited.
WHY_IT_MATTERS: >
  Treating a novice and an expert as interchangeable defeats the purpose of recording a proficiency
  level at all.
DISCONFIRMING_OBSERVATION: >
  Two employees with clearly different recorded proficiency levels in the same skill are ranked or
  presented identically in a staffing suggestion.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Record two employees with materially different proficiency levels in the same skill and request a
  staffing suggestion for a task requiring it.
```

## G12-PROJECT_HR_SKILLS-Q003

```yaml
QID: G12-PROJECT_HR_SKILLS-Q003
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  A skill certification whose recorded expiry date has passed either disqualifies the employee from
  being suggested for a task requiring it, or at minimum produces a visible expiry flag rather than
  being treated identically to a currently valid certification.
WHY_IT_MATTERS: >
  Staffing a regulated or specialized task based on a lapsed certification exposes the business to
  exactly the risk the certification requirement was meant to prevent.
DISCONFIRMING_OBSERVATION: >
  An employee with an expired certification is suggested for a task requiring it with no
  distinguishing flag from an employee whose certification is current.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Record an employee's certification with an expiry date in the past and request a staffing
  suggestion for a task requiring that certification.
```

## G12-PROJECT_HR_SKILLS-Q004

```yaml
QID: G12-PROJECT_HR_SKILLS-Q004
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A task requiring multiple distinct skills at once is matched on all of the named skills together,
  not satisfied by an employee holding only one of them.
WHY_IT_MATTERS: >
  Silently relaxing an "all of these skills" requirement down to "any one of these skills" staffs
  tasks with people who are missing a genuinely required competency.
DISCONFIRMING_OBSERVATION: >
  An employee holding only one of several skills a task requires together is suggested as fully
  matching that task's requirement.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Define a task requiring two distinct skills together and request a staffing suggestion where
  candidates each hold only one of the two.
```

## G12-PROJECT_HR_SKILLS-Q005

```yaml
QID: G12-PROJECT_HR_SKILLS-Q005
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Removing a skill from an employee's central profile after they were assigned to a task requiring
  that skill does not retroactively invalidate the already-made assignment without an explicit review
  step.
WHY_IT_MATTERS: >
  Silently invalidating a live assignment because a central record changed can disrupt in-progress
  work over a data correction that may have nothing to do with actual ongoing suitability.
DISCONFIRMING_OBSERVATION: >
  Removing a skill from an employee's profile automatically unassigns or blocks their existing,
  already in-progress task assignment with no review step.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Assign an employee to a task requiring a skill they hold, then remove that skill from their central
  profile and observe the effect on the existing assignment.
```

## G12-PROJECT_HR_SKILLS-Q006

```yaml
QID: G12-PROJECT_HR_SKILLS-Q006
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A task's record retains the skill level the assignee actually had at the time of assignment, even
  if that employee's central skill record is later changed.
WHY_IT_MATTERS: >
  A historical assignment record that silently rewrites itself to match today's skill level destroys
  the ability to know what was actually true when the staffing decision was made.
DISCONFIRMING_OBSERVATION: >
  After an employee's central skill level changes, a task record from before the change shows the new
  level rather than the one in effect at the time of assignment.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Assign an employee at a recorded skill level, later change that level in their central profile, and
  inspect what the original task record shows.
```

## G12-PROJECT_HR_SKILLS-Q007

```yaml
QID: G12-PROJECT_HR_SKILLS-Q007
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A project manager without HR administrative access can view enough skill information to make a
  staffing decision, without that access extending to broader HR record detail unrelated to staffing.
WHY_IT_MATTERS: >
  Either extreme is a failure: too little visibility blocks legitimate staffing work, too much grants
  unrelated HR access nobody intended.
DISCONFIRMING_OBSERVATION: >
  A project manager account without HR administrative access either cannot see enough skill
  information to staff a task, or can see unrelated HR record detail beyond what staffing requires.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  From a project manager account without HR administrative access, attempt to view skill information
  needed to staff a task.
```

## G12-PROJECT_HR_SKILLS-Q008

```yaml
QID: G12-PROJECT_HR_SKILLS-Q008
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A skill coverage gap between a project's full set of required skills and its actually staffed team
  can be identified through a single report or view, not only discovered task by task through manual
  inspection.
WHY_IT_MATTERS: >
  Requiring a manual task-by-task check to find a coverage gap means gaps are far more likely to go
  unnoticed until they cause a delay.
DISCONFIRMING_OBSERVATION: >
  There is no available report or view that surfaces a project's overall skill coverage gap without
  inspecting each task individually.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create a project with an unmet skill requirement on at least one task and attempt to identify the
  gap through a project-wide view.
```

## G12-PROJECT_HR_SKILLS-Q009

```yaml
QID: G12-PROJECT_HR_SKILLS-Q009
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When no staff member matches a task's required skill, this produces a visible unmet-requirement
  state, rather than silently allowing assignment to proceed with an unqualified person and no flag.
WHY_IT_MATTERS: >
  A silent gap between requirement and reality means the business only discovers the mismatch when
  the unqualified assignment actually fails to deliver.
DISCONFIRMING_OBSERVATION: >
  A task requiring a skill no staff member holds is assigned to someone anyway with no unmet-
  requirement flag anywhere.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Define a task requiring a skill that no available employee holds and attempt to assign it.
```

## G12-PROJECT_HR_SKILLS-Q010

```yaml
QID: G12-PROJECT_HR_SKILLS-Q010
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A skill-based staffing suggestion accounts for an employee's existing workload or allocation, not
  recommending an already fully committed person as if they were freely available.
WHY_IT_MATTERS: >
  A suggestion that ignores availability produces plans that look staffed on paper but cannot
  actually be delivered by the people named.
DISCONFIRMING_OBSERVATION: >
  An employee already fully allocated elsewhere is suggested for a new task with no indication of
  their existing commitment.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Fully allocate an employee to existing work, then request a skill-based staffing suggestion for a
  new task they would otherwise match.
```

## G12-PROJECT_HR_SKILLS-Q011

```yaml
QID: G12-PROJECT_HR_SKILLS-Q011
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When two projects independently identify the same scarce-skill employee as their top candidate at
  the same time, this produces a visible contention rather than a silent double-booking of that
  person to both.
WHY_IT_MATTERS: >
  A silent double-booking of a scarce resource guarantees one of the two projects will be surprised
  by an unavailability nobody flagged in advance.
DISCONFIRMING_OBSERVATION: >
  The same employee is confirmed as assigned to overlapping commitments on two different projects
  with no contention or conflict indicator raised to either.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Have two projects each attempt to confirm the same scarce-skill employee for overlapping
  commitments and observe whether a conflict is surfaced.
```

## G12-PROJECT_HR_SKILLS-Q012

```yaml
QID: G12-PROJECT_HR_SKILLS-Q012
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  An ad hoc, project-level skill tag created outside the central skill catalog stays isolated to that
  project context and does not leak into an employee's central HR skill record without an explicit
  action.
WHY_IT_MATTERS: >
  An informal tag silently becoming part of an employee's permanent HR record blurs the line between
  a quick project note and an official, portable qualification.
DISCONFIRMING_OBSERVATION: >
  A skill tag created only at the project level for a specific need appears in the employee's central
  HR skill record with no explicit action having promoted it there.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create an ad hoc skill tag at the project level for an employee and check whether it appears in
  their central HR skill record.
```

## G12-PROJECT_HR_SKILLS-Q013

```yaml
QID: G12-PROJECT_HR_SKILLS-Q013
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  The permission to edit an employee's central skill record is distinct from, and separately
  grantable from, the permission to merely view skills for staffing purposes.
WHY_IT_MATTERS: >
  Bundling edit rights into ordinary staffing access lets anyone doing project staffing also alter
  the permanent, cross-project record of an employee's qualifications.
DISCONFIRMING_OBSERVATION: >
  An account with only staffing-view access to skill data is able to edit an employee's central skill
  record.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  From an account granted only staffing-view access to skill data, attempt to edit an employee's
  central skill record.
```

## G12-PROJECT_HR_SKILLS-Q014

```yaml
QID: G12-PROJECT_HR_SKILLS-Q014
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Where a skill level maps to a cost or billing rate difference, the rate applied follows the skill
  level actually assigned to the task, not a default rate that ignores it.
WHY_IT_MATTERS: >
  A rate that ignores the actual assigned skill level can either overcharge or undercharge, neither
  of which reflects the true value of the work performed.
DISCONFIRMING_OBSERVATION: >
  Two assignees at clearly different recorded skill levels for the same skill-gated task are billed
  or costed at an identical rate that ignores the level difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Assign two employees at different skill levels to comparable tasks where rate depends on skill
  level, and compare the resulting rates applied.
```

## G12-PROJECT_HR_SKILLS-Q015

```yaml
QID: G12-PROJECT_HR_SKILLS-Q015
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  An external certification nearing expiry produces a reminder that reaches any project the employee
  is actively assigned to under that certification, not only a generic HR-side notice invisible to
  project staffing.
WHY_IT_MATTERS: >
  A reminder that never reaches the project relying on that certification leaves the project team
  blindsided when the certification actually lapses.
DISCONFIRMING_OBSERVATION: >
  An employee's certification nears expiry while actively relied on by a project assignment, and no
  reminder reaches that project context.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Assign a certified employee to a task requiring that certification, let the certification approach
  its expiry, and check whether the project context receives any reminder.
```

## G12-PROJECT_HR_SKILLS-Q016

```yaml
QID: G12-PROJECT_HR_SKILLS-Q016
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Skill data used for staffing decisions is scoped to company boundaries in a multi-company
  environment; an employee's skill record in one company context is not used to staff a project in
  an unrelated company without an explicit cross-company step.
WHY_IT_MATTERS: >
  Skill and personnel data crossing a company boundary without an explicit control undermines the
  same tenant/company separation that governs every other kind of sensitive record.
DISCONFIRMING_OBSERVATION: >
  An employee's skill record scoped to one company appears as a staffing candidate for a project
  scoped to a different, unrelated company with no explicit cross-company authorization.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt to staff a project in one company context using the skill record of an employee scoped to
  a different, unrelated company.
```

## G12-PROJECT_HR_SKILLS-Q017

```yaml
QID: G12-PROJECT_HR_SKILLS-Q017
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  The reasoning behind an automatic staffing suggestion — which skills matched, at what level — is
  available to the person acting on it, not presented as an opaque recommendation with no
  explanation.
WHY_IT_MATTERS: >
  A recommendation nobody can explain cannot be sanity-checked before it is acted on, and cannot be
  defended afterward if it turns out to be wrong.
DISCONFIRMING_OBSERVATION: >
  A staffing suggestion is presented with no accessible explanation of which skills or levels drove
  the recommendation.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Request a skill-based staffing suggestion for a task and attempt to view the reasoning behind the
  suggested candidate.
```

## G12-PROJECT_HR_SKILLS-Q018

```yaml
QID: G12-PROJECT_HR_SKILLS-Q018
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A manual override of an automatic skill-based suggestion is captured along with a reason, and is
  distinguishable afterward from an assignment that simply followed the suggestion.
WHY_IT_MATTERS: >
  An override deserves more scrutiny than a followed suggestion, but only if it can actually be found
  as an override afterward.
DISCONFIRMING_OBSERVATION: >
  An assignment made by overriding the suggested candidate shows no distinguishing record from one
  that simply accepted the suggestion.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Override a skill-based staffing suggestion with a different candidate and inspect the resulting
  record for a distinguishing override indicator.
```

## G12-PROJECT_HR_SKILLS-Q019

```yaml
QID: G12-PROJECT_HR_SKILLS-Q019
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Renaming or merging a skill category in the central catalog does not silently break the ability to
  compare a historical assignment made under the old category name against current staffing data.
WHY_IT_MATTERS: >
  A catalog change that quietly severs the link to historical assignments destroys the ability to do
  any longitudinal analysis of how a skill's use has evolved.
DISCONFIRMING_OBSERVATION: >
  After a skill category is renamed or merged, a historical assignment that relied on the old
  category can no longer be identified as related to the current one.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Rename or merge a skill category that has historical assignment records under it, then attempt to
  trace those records against the new category.
```

## G12-PROJECT_HR_SKILLS-Q020

```yaml
QID: G12-PROJECT_HR_SKILLS-Q020
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  A bulk update to skill records across many employees at once produces per-employee audit detail,
  not a single undifferentiated bulk log entry.
WHY_IT_MATTERS: >
  A single bulk log line makes it impossible to determine afterward exactly which employees' skill
  data actually changed and how.
DISCONFIRMING_OBSERVATION: >
  A bulk skill-record update across several employees produces one generic log entry with no way to
  see which specific employees and values changed.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Perform a bulk skill-record update across several employees and inspect the resulting audit detail.
```

## G12-PROJECT_HR_SKILLS-Q021

```yaml
QID: G12-PROJECT_HR_SKILLS-Q021
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Where a required skill's associated certification standard differs by locale (an international
  versus a domestic standard), the matching logic treats a valid certification under either standard
  consistently, rather than silently favoring one.
WHY_IT_MATTERS: >
  Silently favoring one locale's standard could unfairly exclude equally qualified staff certified
  under the other.
DISCONFIRMING_OBSERVATION: >
  Two employees each holding an equivalent, currently valid certification under different locale
  standards are treated inconsistently by the same skill-matching requirement.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record two employees with equivalent certifications issued under different locale standards and
  match them against the same skill requirement.
```

## G12-PROJECT_HR_SKILLS-Q022

```yaml
QID: G12-PROJECT_HR_SKILLS-Q022
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A skill development or training goal tied to an employee's record can reference relevant project
  experience without requiring the same information to be manually re-entered a second time.
WHY_IT_MATTERS: >
  Forced duplicate entry of the same experience information invites drift between the two records
  and discourages people from keeping either one current.
DISCONFIRMING_OBSERVATION: >
  Linking a training goal to project experience already on record requires manually re-entering
  information that already exists elsewhere in the system.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt to link an employee's training goal to project experience already recorded elsewhere in the
  system.
```

## G12-PROJECT_HR_SKILLS-Q023

```yaml
QID: G12-PROJECT_HR_SKILLS-Q023
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Completing a project task that exercised a specific skill does not automatically alter the
  employee's central skill record without an explicit confirming step.
WHY_IT_MATTERS: >
  An automatic, unreviewed change to a permanent qualification record based only on task completion
  could credit a skill level nobody actually verified.
DISCONFIRMING_OBSERVATION: >
  An employee's central skill record changes immediately upon completing a related task, with no
  confirming step by any responsible party.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Complete a task tied to a specific skill and check whether the employee's central skill record
  changes without a confirming action.
```

## G12-PROJECT_HR_SKILLS-Q024

```yaml
QID: G12-PROJECT_HR_SKILLS-Q024
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Where both a self-assessed skill level and a manager-assessed skill level exist for the same
  employee, the staffing logic uses one at a defined, documented precedence, not an inconsistent pick
  between the two.
WHY_IT_MATTERS: >
  An unpredictable choice between two different assessments of the same skill undermines confidence
  in any staffing decision built on it.
DISCONFIRMING_OBSERVATION: >
  Two comparable staffing decisions each pick a different one of the two available assessed levels
  for the same employee's skill with no documented rule explaining the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record both a self-assessed and a manager-assessed level for the same employee's skill and observe
  which one governs across two comparable staffing decisions.
```

## G12-PROJECT_HR_SKILLS-Q025

```yaml
QID: G12-PROJECT_HR_SKILLS-Q025
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Sensitive skill-related data, such as a third-party certification identifier, is not exposed in a
  project-facing staffing view beyond what is actually needed to confirm eligibility.
WHY_IT_MATTERS: >
  A certification identifier is exactly the kind of detail that has no staffing purpose beyond
  confirming validity, and over-exposing it multiplies the ways it can leak.
DISCONFIRMING_OBSERVATION: >
  A project-facing staffing view displays a certification's full identifier where only validity
  status would be needed.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Inspect a project-facing staffing view for an employee with a recorded third-party certification
  and check what level of detail is actually exposed.
```

## G12-PROJECT_HR_SKILLS-Q026

```yaml
QID: G12-PROJECT_HR_SKILLS-Q026
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  An employee can see enough of their own skill-match information relevant to their own assignment to
  understand why they were selected, without that visibility extending to other employees' equivalent
  detail.
WHY_IT_MATTERS: >
  An employee with no visibility into why they were picked cannot raise a legitimate objection, while
  visibility into others' data goes beyond what their own assignment requires.
DISCONFIRMING_OBSERVATION: >
  An employee cannot see any explanation of their own skill-based selection, or can see the equivalent
  detail for other employees beyond their own assignment.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  From an ordinary employee account, attempt to view the skill-match explanation for their own
  assignment and for another employee's.
```

## G12-PROJECT_HR_SKILLS-Q027

```yaml
QID: G12-PROJECT_HR_SKILLS-Q027
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A mid-project change to a task's required skill flags the existing assignment for review, rather
  than leaving a now-mismatched assignment unexamined and untouched.
WHY_IT_MATTERS: >
  A requirement that changes without revisiting who is actually staffed against it can leave a task
  quietly worked by someone who no longer meets the stated need.
DISCONFIRMING_OBSERVATION: >
  Changing a task's required skill after assignment leaves the existing, now-mismatched assignee in
  place with no review flag raised.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Assign an employee to a task, then change the task's required skill to one the assignee does not
  hold, and observe whether a review is flagged.
```

## G12-PROJECT_HR_SKILLS-Q028

```yaml
QID: G12-PROJECT_HR_SKILLS-Q028
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A shared resource pool spanning many projects prevents the same skilled individual from being
  confirmed to two overlapping commitments without a visible conflict indicator at the point of the
  second confirmation.
WHY_IT_MATTERS: >
  Confirming a second overlapping commitment with no warning guarantees one project will discover the
  conflict only when the work fails to happen.
DISCONFIRMING_OBSERVATION: >
  An employee is confirmed to a second, overlapping commitment on a different project with no conflict
  indicator raised at the point of that confirmation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an employee to a commitment on one project, then attempt to confirm the same employee to an
  overlapping commitment on a different project.
```

## G12-PROJECT_HR_SKILLS-Q029

```yaml
QID: G12-PROJECT_HR_SKILLS-Q029
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  The ability to create a new skill category in the central catalog is governed by a defined
  permission, not open to anyone performing ordinary project staffing.
WHY_IT_MATTERS: >
  An uncontrolled ability to create new skill categories leads to an uncurated, inconsistent catalog
  that undermines the value of matching against it at all.
DISCONFIRMING_OBSERVATION: >
  An account with only ordinary project-staffing access is able to create a new skill category in the
  central catalog.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  From an account with only ordinary project-staffing access, attempt to create a new skill category
  in the central catalog.
```

## G12-PROJECT_HR_SKILLS-Q030

```yaml
QID: G12-PROJECT_HR_SKILLS-Q030
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A deactivated or retired skill category does not silently disappear from historical assignment
  records that relied on it at the time.
WHY_IT_MATTERS: >
  Losing the historical trace of a retired category makes it impossible to later understand what a
  past assignment was actually staffed against.
DISCONFIRMING_OBSERVATION: >
  A historical assignment made against a skill category that has since been retired no longer shows
  which category it was originally matched against.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Retire a skill category that has historical assignment records against it, then inspect those
  records for the original category reference.
```

## G12-PROJECT_HR_SKILLS-Q031

```yaml
QID: G12-PROJECT_HR_SKILLS-Q031
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Where an employee holds a skill at multiple recorded levels from different sources (self-declared,
  tested, manager-confirmed), the assignment record shows which source's level was actually used for
  that assignment.
WHY_IT_MATTERS: >
  Not knowing which of several conflicting level sources actually governed a staffing decision
  prevents any later audit of whether the decision was well-founded.
DISCONFIRMING_OBSERVATION: >
  An assignment record for an employee with multiple recorded skill-level sources does not indicate
  which source's level was actually used.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record multiple differing skill-level sources for the same employee, make an assignment, and inspect
  which source is identified as governing.
```

## G12-PROJECT_HR_SKILLS-Q032

```yaml
QID: G12-PROJECT_HR_SKILLS-Q032
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A project template that pre-defines required skills for its standard tasks applies those
  requirements consistently to every project actually created from it, not inconsistently between
  instances.
WHY_IT_MATTERS: >
  An inconsistently applied template requirement means the same "standard" task can silently demand
  different qualifications on different projects for no reason anyone chose.
DISCONFIRMING_OBSERVATION: >
  Two projects created from the identical template show different required skills on the same
  standard task with no documented customization made.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create two separate projects from the same template and compare the required skills on their
  equivalent standard tasks.
```

## G12-PROJECT_HR_SKILLS-Q033

```yaml
QID: G12-PROJECT_HR_SKILLS-Q033
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  An employee's skill-based eligibility for a task does not override an independent role-based
  restriction that would otherwise prevent them from being assigned that type of task.
WHY_IT_MATTERS: >
  Letting a matched skill silently bypass a role restriction defeats the purpose of having a role-based
  control at all.
DISCONFIRMING_OBSERVATION: >
  An employee who holds the required skill but is barred by a role-based restriction is still
  successfully assigned to the task.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Configure a role-based restriction on a task type, then attempt to assign an employee who holds the
  required skill but not the required role.
```

## G12-PROJECT_HR_SKILLS-Q034

```yaml
QID: G12-PROJECT_HR_SKILLS-Q034
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Skill matching for a task considers only currently valid certifications — excluding one formally
  retracted by its issuing body — not any certification ever recorded regardless of its current
  standing.
WHY_IT_MATTERS: >
  Matching against a formally retracted certification staffs a task on a qualification the issuing
  authority itself no longer stands behind.
DISCONFIRMING_OBSERVATION: >
  An employee whose certification has been formally retracted is still matched for a task requiring
  it, identically to one whose certification remains valid.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Mark an employee's certification as formally retracted and request a staffing match for a task
  requiring it.
```

## G12-PROJECT_HR_SKILLS-Q035

```yaml
QID: G12-PROJECT_HR_SKILLS-Q035
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An employee's approved leave or recorded unavailability overlapping the project's timeframe is
  factored into a skill-based staffing suggestion, not ignored simply because their skill matches.
WHY_IT_MATTERS: >
  A suggestion that ignores known unavailability recommends someone who cannot actually do the work
  when it is needed.
DISCONFIRMING_OBSERVATION: >
  An employee with recorded, approved unavailability overlapping the project timeframe is suggested
  for a task with no indication of the conflict.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Record approved leave overlapping a project's timeframe for an otherwise well-matched employee and
  request a staffing suggestion for a task in that timeframe.
```

## G12-PROJECT_HR_SKILLS-Q036

```yaml
QID: G12-PROJECT_HR_SKILLS-Q036
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An automatic skill-matching process that fails to run, due to a configuration or data issue,
  produces a visible failure state to the staffing user, distinguishable from a genuine result of no
  qualified match.
WHY_IT_MATTERS: >
  A failure indistinguishable from a true no-match result could be mistaken for confirmation that no
  one is qualified, when actually the check never ran at all.
DISCONFIRMING_OBSERVATION: >
  A skill-matching process that fails to run due to a configuration or data issue presents identically
  to a genuine no-match result, with nothing distinguishing the two.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Introduce a configuration or data condition that would cause the matching process to fail to run,
  and compare the resulting screen to a genuine no-match case.
```

## G12-PROJECT_HR_SKILLS-Q037

```yaml
QID: G12-PROJECT_HR_SKILLS-Q037
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A skill required at the project level (a general competency) and a skill required at the task level
  (a specific competency) are matched independently, and the task-level requirement is not silently
  satisfied merely because the project-level one is met.
WHY_IT_MATTERS: >
  Collapsing a specific task-level requirement into a general project-level one can staff a
  specialized task with someone who only meets the broader, easier bar.
DISCONFIRMING_OBSERVATION: >
  An employee who meets only the project's general skill requirement, but not a specific task-level
  requirement, is presented as fully matching that task.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Define a project-level general skill requirement and a stricter task-level requirement, then match
  an employee who satisfies only the general one.
```

## G12-PROJECT_HR_SKILLS-Q038

```yaml
QID: G12-PROJECT_HR_SKILLS-Q038
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Concurrent edits to the same employee's skill record by two different people (for example, HR and a
  certifying manager) do not result in one edit being silently lost with neither party notified of a
  conflict.
WHY_IT_MATTERS: >
  A silently lost concurrent edit to a qualification record can leave the record wrong with no one
  aware their update never actually took effect.
DISCONFIRMING_OBSERVATION: >
  Two concurrent edits to the same employee's skill record result in one disappearing with neither
  editor notified of a conflict.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Open the same employee's skill record in two sessions and submit conflicting edits at nearly the
  same time.
```

## G12-PROJECT_HR_SKILLS-Q039

```yaml
QID: G12-PROJECT_HR_SKILLS-Q039
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  A skill catalog import or migration that introduces new skill identifiers does not silently
  disconnect existing assignments from the skill they were originally matched against.
WHY_IT_MATTERS: >
  A migration that breaks the link between a historical assignment and its matched skill destroys the
  ability to later confirm what a staffing decision was actually based on.
DISCONFIRMING_OBSERVATION: >
  After a skill catalog import or migration, an existing assignment's link to its originally matched
  skill can no longer be resolved.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Perform a skill catalog import or migration affecting a skill with existing assignment history, then
  inspect whether that history's link to the skill still resolves.
```

## G12-PROJECT_HR_SKILLS-Q040

```yaml
QID: G12-PROJECT_HR_SKILLS-Q040
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  The staffing suggestion logic's own configuration — which factors it weighs, such as skill level
  versus availability — is discoverable, rather than an unexplained black box that produces
  different-seeming results with no visible reason.
WHY_IT_MATTERS: >
  An undiscoverable weighting scheme means no one can explain, defend, or intentionally tune why the
  suggestion behaves the way it does.
DISCONFIRMING_OBSERVATION: >
  There is no way to determine which factors the staffing suggestion logic weighs or how, when two
  comparable cases produce different-seeming rankings.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Attempt to determine what factors and weighting the staffing suggestion logic uses by comparing its
  output across varied comparable cases.
```

## G12-PROJECT_HR_SKILLS-Q041

```yaml
QID: G12-PROJECT_HR_SKILLS-Q041
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  An employee who is deactivated (leaves the company) is removed from active staffing suggestions
  going forward, while their historical assignment records remain fully intact.
WHY_IT_MATTERS: >
  Continuing to suggest a departed employee wastes staffing effort, while losing their historical
  record destroys past project accountability.
DISCONFIRMING_OBSERVATION: >
  A deactivated employee still appears in new staffing suggestions, or their historical assignment
  records disappear or degrade upon deactivation.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Deactivate an employee with prior assignment history and check both new staffing suggestions and
  their historical record.
```

## G12-PROJECT_HR_SKILLS-Q042

```yaml
QID: G12-PROJECT_HR_SKILLS-Q042
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A skill requirement expressed as "any one of several acceptable skills" is evaluated distinctly
  from one expressed as "all of these skills required," and the two are not silently conflated into
  the same matching behaviour.
WHY_IT_MATTERS: >
  Conflating an OR requirement with an AND requirement either wrongly excludes qualified candidates or
  wrongly admits unqualified ones.
DISCONFIRMING_OBSERVATION: >
  A task configured to require "any one of" several skills is matched using "all of" logic, or vice
  versa, producing the wrong set of eligible candidates.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Configure one task with an "any one of" skill requirement and another with an "all of" requirement,
  using the same set of skills, and compare the resulting matches.
```

## G12-PROJECT_HR_SKILLS-Q043

```yaml
QID: G12-PROJECT_HR_SKILLS-Q043
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  When a certifying body or standard is later found invalid or revoked after certifications under it
  were already recorded, the affected employees' eligibility for skill-gated tasks is flagged for
  review rather than left unexamined indefinitely.
WHY_IT_MATTERS: >
  An unreviewed population of now-questionable certifications leaves skill-gated staffing decisions
  resting on a foundation nobody has actually re-checked.
DISCONFIRMING_OBSERVATION: >
  Certifications recorded under a since-revoked standard remain fully trusted for staffing with no
  review flag raised for the affected employees.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Mark a certifying standard as revoked after employees already hold certifications under it, and
  check whether their eligibility is flagged for review.
```

## G12-PROJECT_HR_SKILLS-Q044

```yaml
QID: G12-PROJECT_HR_SKILLS-Q044
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A skill-based candidate suggestion for a task is reachable and behaves the same way regardless of
  which entry point — a task's own screen, a project-wide staffing view, or a resource-planning view —
  the request is made from.
WHY_IT_MATTERS: >
  A suggestion that differs by entry point gives inconsistent staffing advice depending on which
  screen someone happens to be using.
DISCONFIRMING_OBSERVATION: >
  Requesting a skill-based suggestion for the same task from two different entry points produces
  different results with no explained reason.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Request a skill-based staffing suggestion for the same task from at least two different available
  entry points and compare the results.
```

## G12-PROJECT_HR_SKILLS-Q045

```yaml
QID: G12-PROJECT_HR_SKILLS-Q045
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A skill-based staffing recommendation does not silently ignore an employee's own stated preference
  to not be assigned to a particular type of project or task, where such a preference is recorded.
WHY_IT_MATTERS: >
  Ignoring a recorded preference the business chose to capture makes recording it a pointless gesture
  with no actual effect on staffing outcomes.
DISCONFIRMING_OBSERVATION: >
  An employee with a recorded preference against a particular task type is suggested for exactly that
  type with no indication their preference was considered.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Record an employee's stated preference against a particular task type and request a staffing
  suggestion for a task of that type where the employee otherwise matches.
```

## G12-PROJECT_HR_SKILLS-Q046

```yaml
QID: G12-PROJECT_HR_SKILLS-Q046
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The audit trail for a skill-based staffing decision retains which candidates were considered, not
  only which one was ultimately chosen.
WHY_IT_MATTERS: >
  Without knowing who else was considered, a reviewer cannot judge whether the final choice was
  actually the best available match or simply the only one anyone looked at.
DISCONFIRMING_OBSERVATION: >
  The audit record of a staffing decision shows only the final assignee, with no trace of which other
  candidates were considered.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Make a staffing decision from a pool of multiple matching candidates and inspect the audit record
  for whether the full candidate set is retained.
```

## G12-PROJECT_HR_SKILLS-Q047

```yaml
QID: G12-PROJECT_HR_SKILLS-Q047
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A required skill tied to a safety, compliance, or regulated task blocks assignment of a
  non-qualified person outright, rather than producing only a dismissible advisory warning that can be
  clicked past.
WHY_IT_MATTERS: >
  A warning that can simply be dismissed provides no real protection against staffing a regulated task
  with an unqualified person.
DISCONFIRMING_OBSERVATION: >
  Assigning a non-qualified person to a task tied to a safety or regulated requirement succeeds after
  only a dismissible warning, with no hard block.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt to assign a person lacking the required qualification to a task tied to a safety or
  regulated requirement.
```

## G12-PROJECT_HR_SKILLS-Q048

```yaml
QID: G12-PROJECT_HR_SKILLS-Q048
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Where an employee's skill record is inherited from an external system feed, an outage or delay in
  that feed produces a visibly stale-data indicator, rather than presenting the last-known data as
  fully current with no distinction.
WHY_IT_MATTERS: >
  Data presented as current when it is actually stale can lead to a staffing decision based on
  qualifications that may no longer be accurate.
DISCONFIRMING_OBSERVATION: >
  Skill data known to be stale due to a feed outage is presented identically to freshly updated data,
  with no staleness indicator.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Simulate an outage or delay in the external feed supplying an employee's skill data and inspect
  whether staleness is indicated anywhere.
```

## G12-PROJECT_HR_SKILLS-Q049

```yaml
QID: G12-PROJECT_HR_SKILLS-Q049
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Merging two employee records believed to represent the same person, where each carries different
  recorded skill data, surfaces the conflict rather than silently choosing one side's skill data as
  authoritative.
WHY_IT_MATTERS: >
  A silent choice between two conflicting skill records during a merge could quietly discard a
  genuinely held, verified qualification.
DISCONFIRMING_OBSERVATION: >
  Merging two employee records with differing skill data picks one side silently with no surfaced
  conflict or choice presented.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create two employee records for the same person with different recorded skill data and merge them.
```

## G12-PROJECT_HR_SKILLS-Q050

```yaml
QID: G12-PROJECT_HR_SKILLS-Q050
MODULE: project_hr_skills
TYPE: MODULE
AUTHOR: P12-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The complete basis for why a specific individual was ultimately assigned to a skill-gated task —
  matched skill, level, availability, and any manual override — can be reconstructed end to end from
  stored records alone.
WHY_IT_MATTERS: >
  If this basis cannot be reconstructed, a later dispute or audit of a skill-gated assignment has
  nothing but recollection to rely on.
DISCONFIRMING_OBSERVATION: >
  Attempting to reconstruct the full basis for a skill-gated assignment — matched skill, level,
  availability, and any override — leaves gaps that stored records alone cannot fill.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Make a skill-gated assignment involving a manual override, then attempt to reconstruct the full
  basis for that assignment using only stored records.
```
