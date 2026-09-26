# G01 Recovery QID Trace Matrix C1

Date: 2026-09-27
Status: TRACE CONTROL ONLY / NOT PRIMARY EVIDENCE / NOT QID PASS

| QID | Evidence trace | Boundary |
|---|---|---|
| G01-BASE-Q004 | R2 AKU 6-7 | static source support only; runtime required |
| G01-BASE-Q005 | R2 AKU 3,7 | static source support only; runtime required |
| STD-Q45 | R2 AKU 4-5,12-14 | unattended execution source support; runtime/config proof required |
| G01-MAIL-Q023 | R1 MAIL-AKU-005; R2 AKU 8,11 | message/recipient access source support; UI notification proof required |
| G01-MAIL-Q032 | R2 AKU 12,14; R3 AKU 14 | scheduled/queue source support; retry context proof required |
| G01-MAIL-Q048 | R1 MAIL-AKU-005; R2 AKU 8,11 | source access support; counter-side-channel proof required |
| G01-MAIL-Q050 | R1 MAIL-AKU-002/003/005; R2 AKU 8-14; R3 AKU 12-15 | multiple communication paths identified; equivalence proof required |

Governed question sources:
- G01_BASE_GMVQ_MVQ_50_V1.00_DRAFT.md
- QUESTION_BANK_STANDARD_55_V2.00.md
- G01_MAIL_GMVQ_MVQ_50_V1.00_DRAFT.md

All seven QIDs were revalidated in the governed question banks.
PR #68 independent review remains pending.
A1 Single Exit remains NOT READY.
A2 and Formal Coverage remain NOT AUTHORIZED.
