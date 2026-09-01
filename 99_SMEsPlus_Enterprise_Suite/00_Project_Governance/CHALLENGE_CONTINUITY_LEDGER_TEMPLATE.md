# SMEsPlus Challenge Continuity Ledger Template

Document ID: `SMEPLUS-GOV-CHALLENGE-LEDGER-001`  
Version: `1.0`  
Status: `BOSS APPROVED CONTROL TEMPLATE`  
Control Level: `/L999.999`  
Governing Standard: `STATE03_PLUS_PRE_PROMPT_INDEPENDENT_CHALLENGE_RULE.md v2.0`  
Final Approval Authority: `Boss`

---

## 1. Purpose

This ledger preserves challenge learning across Sessions and Prompts so challenge does not restart from zero and previously resolved questions are not repeatedly asked without a material delta.

Hard rules:

`No reset-to-zero challenge.`  
`No repeated question without a material delta.`  
`Historical challenge records must not be deleted.`

---

## 2. Mandatory Ledger Fields

| Challenge_ID | Council_Mandate | Question_Fingerprint | Question | First_Raised_In | Risk | Evidence_Required | Status | Resolution_Evidence | Boss_Decision | Carry_Forward | Last_Reviewed_In | Delta_Trigger | Reopen_Reason | Affected_Scope_or_Gate | Special_Team_Activated | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | NEW | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

---

## 3. Controlled Status Vocabulary

Use only:

- `NEW`
- `OPEN`
- `EVIDENCE_REQUIRED`
- `CONFLICTING_EVIDENCE`
- `CARRY_FORWARD`
- `RESOLVED`
- `CLOSED_WITH_EVIDENCE`
- `REOPENED_WITH_DELTA`
- `SUPERSEDED`
- `DUPLICATE_SUPPRESSED`

---

## 4. Question Fingerprint Rule

A Question Fingerprint identifies the underlying material question independently of wording.

Before creating a new Challenge ID, PMO must compare the proposed question against prior ledger entries by:

- business subject;
- affected object / domain;
- risk / failure mode;
- evidence needed;
- affected Gate / authority.

If materially the same question already exists and no Delta Trigger exists:

`DUPLICATE_SUPPRESSED`.

Do not create a cosmetic rewording as a new challenge.

---

## 5. Reopen Rule

A closed question may be reopened only with a documented Delta Trigger such as:

- new contradictory evidence;
- Boss ruling / baseline change;
- Scope / dependency change;
- regression;
- provisional prior resolution;
- evidence integrity loss;
- regulatory / authoritative evidence change;
- discovery that the prior closure lacked adequate evidence.

Every reopen entry must reference the prior Challenge ID and answer:

1. `Why reopened now?`
2. `What changed?`
3. `What evidence must now be re-examined?`

---

## 6. Per-Prompt Delta Summary

For every controlled Prompt / Session, record one concise delta block:

```text
Prompt / Session ID:
Parent Prompt / Session:
Previous Ledger Reference:
New Boss Intent Delta:
New Evidence Delta:
Scope / Authority Delta:
New Challenges:
Reopened Challenges:
Duplicate Questions Suppressed:
Carry-Forward Challenges:
Special Teams Activated:
Readiness Status:
Final Prompt Evidence Reference:
```

If nothing material changed:

`NO NEW MATERIAL CHALLENGE — PRIOR CONTROLLED QUESTIONS CARRIED FORWARD.`

---

## 7. Governance

`Challenge First -> Prompt Second -> Execution Third.`  
`Special Team investigates; Council challenges; PMO preserves; Boss decides.`  
`No Challenge Evidence = No Controlled Prompt Execution.`  
`No Evidence = No Progress.`  
`Never Skip Gate.`  
`Boss = Sole Final Approver.`
