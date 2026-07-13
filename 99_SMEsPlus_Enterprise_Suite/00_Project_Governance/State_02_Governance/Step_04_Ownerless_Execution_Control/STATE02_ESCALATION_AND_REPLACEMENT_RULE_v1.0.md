# STATE02_ESCALATION_AND_REPLACEMENT_RULE_v1.0.md

Session: SMEPLUS-26-07-13-007
State: 02 — Governance
Step: 04 — Ownerless Execution Control
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Target Branch: SMEsPlus
Intake Branch: claude/state-02-step-03-04-sn0sr1
Reference Base Commit: 5454d2afb2efb4d5f2def0a744981b812b843982
Prepared By: Claude AI (Responsible role only)
Prepared At: 2026-07-13T16:16Z (UTC)
Document Status: PREPARED FOR REVIEW
Gate Status: HOLD — REVIEW AND VERIFICATION PENDING

## 1. Escalation Clocks

| Priority | Inactivity Trigger | Action |
|---|---|---|
| P0 | No action or evidence within 20 minutes | Escalate; AI Execution Agent may continue permitted operational work with evidence; Acting Owner appointment (if needed) requires explicit Boss authorization |
| P1 | No action or evidence within 4 working hours | Escalate; prepare Acting Owner recommendation and Boss decision request; appointment requires explicit Boss authorization |
| P2 | No action or evidence within 1 working day | Escalate; prepare owner replacement review package for Boss decision |

Clock start: the moment the work item is assigned or its upstream dependency clears.
Clock stop: the moment evidence is recorded, or a valid blocker with evidence is
reported (`BLOCKED WITH EVIDENCE` — the owner is NOT classified inactive).

## 2. Escalation Ladder

```text
Level 0: Assigned Owner (evidence within priority window)
Level 1: Executive Secretary / Liza — coordination and escalation only; prepares the
         acting-owner recommendation but does not appoint or activate one
Level 2: Replacement per STATE02_OWNER_REPLACEMENT_MATRIX_v1.0.md (Acting Owner
         appointment requires explicit Boss authorization)
Level 3: Authorized AI Execution Agent for all permitted operational work
Level 4: Alternate AI / system connector with real execution capability
Level 5: Boss — ONLY non-delegable decisions (authorization, credentials, appointments
         with authority impact, Gate approval). Never routine operational work.
```

## 3. Escalation Content Requirements

Every escalation record must contain: Work ID, priority, clock start/expiry
timestamps, owner, evidence requested, evidence received (or NONE), proposed
replacement, and the single decision required (if Level 5).

## 4. Replacement Activation Rules

1. Replacement transfers only the operational (Responsible) duty — never the
   Accountable role and never any approval authority. Reassignment of the
   Accountable role requires Boss authorization; Executive Secretary / Liza may
   prepare the reassignment record but may not reassign it independently.
2. The replaced owner's inactivity is recorded in the Ownerless Work Register with
   evidence of the missed window.
3. A replacement executor must record evidence (commit SHA, register entry, system
   record) for every action, exactly as the original owner would.
4. Reviewer/Verifier replacement must preserve independence: the replacement must not
   be the preparer of the work under review.
5. When no execution-capable agent exists, ONLY the missing authorization/tool
   decision escalates to Boss, packaged as a single yes/no decision.

## 5. Anti-Patterns Explicitly Prohibited

```text
Sending Boss routine operational work.
Marking an item resolved because a replacement was assigned (evidence still required).
Replacing a Reviewer or Verifier with the preparer.
Treating an evidence-free progress report as activity.
Using owner inactivity to bypass Boss approval on non-delegable decisions.
```

## 6. Control Statement

PREPARED FOR REVIEW. Effective only after independent review, verification, and Boss
approval. Boss is the Sole Final Approver.
