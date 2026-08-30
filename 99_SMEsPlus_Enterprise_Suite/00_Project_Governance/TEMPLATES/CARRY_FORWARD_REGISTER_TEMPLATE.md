# CARRY-FORWARD REGISTER TEMPLATE

Template ID: SMEPLUS-TPL-CF-001
Version: v1.0
Status: BOSS APPROVED / MANDATORY TEMPLATE
Effective Date: 2026-08-30
Governing Policy: `SMEPLUS-POL-CF-001`

## Register

| CF ID | Source STATE/STEP | Gap / Risk / Open Item | Reason for Deferral | Classification | Target STATE/STEP | Accountable Owner | Responsible Team | Required Deliverable | Acceptance Criteria | Due Date / Trigger | Dependencies | Evidence Requirement / Path | Gate Impact | Receiver Acceptance | Acceptance Evidence / Date | Age / Days Open | Overdue | Deferral Count | Status | Boss Ruling Ref |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---:|---|---:|---|---|
| CF-XXXX | TBD | TBD | TBD | CARRY FORWARD | TBD | UNASSIGNED | TBD | TBD | TBD | TBD | TBD | TBD | TBD | NOT ACCEPTED | TBD | TBD | TBD | 0 | OWNER ASSIGNMENT REQUIRED | N/A |

## Validation Checklist

A record may be marked `CARRY FORWARD ACCEPTED` only when all checks are YES:

| Check | YES/NO | Evidence / Note |
|---|---|---|
| Target STATE/STEP identified |  |  |
| Accountable Owner named |  |  |
| Responsible Team named |  |  |
| Deliverable defined |  |  |
| Acceptance Criteria defined |  |  |
| Due Date / Trigger defined |  |  |
| Dependencies recorded |  |  |
| Evidence requirement/path defined |  |  |
| Gate impact recorded |  |  |
| Receiver explicitly accepted |  |  |
| Receiver acceptance evidence recorded |  |  |
| Item registered in target baseline/register |  |  |

Any `NO`, `TBD`, or `UNASSIGNED` in a mandatory field means the handoff is not accepted and the source item remains open.

## Status Flow

```text
PROPOSED
→ OWNER ASSIGNMENT REQUIRED / RECEIVER REVIEW REQUIRED
→ CARRY FORWARD ACCEPTED
→ SCHEDULED / TRIGGERED
→ IN PROGRESS
→ EVIDENCE REVIEW
→ VERIFIED
→ CLOSED
```

Exception statuses:

```text
REJECTED / RETURN TO SOURCE
OVERDUE
ESCALATED TO BOSS
```

## Re-Deferral Control

If `Deferral Count >= 2`, Boss Review is mandatory before the item can be moved again.

## Core Rule

**No Owner = No Carry Forward**  
**No Receiver Acceptance = No Handoff**  
**No Due/Trigger = No Schedule**  
**No Acceptance Criteria = No Closure**
