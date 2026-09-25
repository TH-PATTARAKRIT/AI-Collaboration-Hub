# STATE04 ROLE & STATUS TERMINOLOGY

Version: v1.0  
Status: Approved Working Standard  
Owner: Executive Secretary / SMEsPlus PMO  
Authority: Boss-approved STATE04 organization baseline  
Effective Date: 2026-08-30  
Scope: STATE04 Design Organization and Team11 Audit Veto controls

## Purpose

Define consistent English/Thai meanings for staffing, evidence and gate terms used across STATE04 so `TBD`, `UNASSIGNED`, `N/A`, `HOLD` and related terms cannot be misread as progress.

## Mandatory Terms

| Term | English Meaning | Thai Meaning | Control Meaning |
|---|---|---|---|
| `TBD` | To Be Determined | ยังไม่กำหนด | Required detail is known to exist but has not yet been determined. No schedule/progress credit for that field. |
| `UNASSIGNED` | No accountable person/AI role appointed yet | ยังไม่ได้แต่งตั้งผู้รับผิดชอบ | Role exists, but no accountable owner is assigned. Ownerless work cannot pass an Evidence Gate. |
| `ASSIGNED` | Accountable owner formally appointed and evidenced | แต่งตั้งผู้รับผิดชอบแล้ว | Must have owner identity, evidence location and effective timestamp. |
| `N/A` | Not Applicable after review | ตรวจแล้วว่าไม่อยู่ในขอบเขต | Requires reviewer, reason and evidence. Silence/omission is never N/A. |
| `DRAFT` | Work exists but is not verified | ร่าง / ยังไม่ผ่านการตรวจ | No PASS credit. |
| `IN REVIEW` | Independent review is active | อยู่ระหว่างตรวจสอบ | Gate remains open/HOLD until disposition. |
| `HOLD` | Evidence exists but a required review/linkage/control remains incomplete | พัก / ยังผ่านไม่ได้ | Progression blocked until stated condition is closed. |
| `RETURN FOR REWORK` | Reviewer found correctable defects | ส่งกลับแก้ไข | Responsible Design Team must correct and resubmit. |
| `VETO` | Independent Audit Veto blocks normal progression | ยับยั้งการผ่าน Gate | Design cannot freeze or enter STATE05/STATE06 unless corrected or Boss records explicit written override/risk acceptance. |
| `PASS WITH CONTROL` | Review scope is sufficiently verified with explicit controlled carry-forward | ผ่านแบบมีเงื่อนไขควบคุม | Carry-forward must have owner, due date/accepted permanent control, evidence and gate impact. |
| `PASS` | Required evidence exists, is accessible, timestamped and independently verified | ผ่านตามหลักฐาน | Does not equal Boss final approval. |
| `BOSS APPROVED` | Boss has issued explicit final decision for the stated scope | บอสอนุมัติในขอบเขตที่ระบุ | Scope-specific only; cannot be generalized to build/release/production unless explicitly stated. |

## Mandatory Staffing Interpretation

```text
Role exists + no owner       = UNASSIGNED
Need/detail not yet decided  = TBD
Reviewed and irrelevant      = N/A + evidence
Evidence missing             = NO PROGRESS
Reviewer not independent     = INVALID REVIEW
```

## Team11 Rule

Every D0-D3 review cycle must record the actual reviewer identity. The existence of an expert capability or charter alone does not prove that a specific review cycle was independently executed.

## Governing Principles

No Evidence = No Progress.  
Never Skip Gate.  
Independent Reviewer must not review its own work.  
Boss = Sole Final Approver.
