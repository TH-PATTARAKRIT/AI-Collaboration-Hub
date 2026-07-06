# (split from combined source — see SOURCE_COMBINED_FILE_NOTE.md)

# SMEsPlus Master Template Index L99

| Field | Value |
| --- | --- |
| Project | SMEsPlus Enterprise Suite |
| Document ID | SMEPLUS-IDX-L99-002 |
| Version | v2.0 |
| Status | READY FOR REVIEW |
| Gate Status | HOLD UNTIL FINAL REVIEW |
| Control Level | /L99 |
| Owner | PMO Evidence Controller |
| Reviewer | Enterprise Architect / Technical PMO Director |
| Approver | Boss / Final Gate Owner |
| Evidence Path | 99\_SMEsPlus\_Enterprise\_Suite/00\_Master\_Templates/ |
| Traceability | Template Index -> Template Usage -> Evidence -> Gate Review |

## Template Catalogue

| No. | File | Purpose | Required Use Case | Gate Status |
| --- | --- | --- | --- | --- |
| 1 | README.md | Folder overview and usage control | Explain package and gate status | HOLD |
| 2 | 00\_TEMPLATE\_INDEX.md | Template list and usage matrix | Select correct template before execution | HOLD |
| 3 | SMEPLUS\_MASTER\_TEMPLATE\_STANDARD\_L99\_v2.0.md | Enterprise master standard | All SMEsPlus documents | HOLD |
| 4 | SMEPLUS\_EVIDENCE\_REGISTER\_TEMPLATE\_L99.md | Evidence tracking | Any workstream claiming progress | HOLD |
| 5 | SMEPLUS\_TRACEABILITY\_MATRIX\_TEMPLATE\_L99.md | Requirement-to-evidence mapping | Functional, design, development, QA, gate | HOLD |
| 6 | SMEPLUS\_GATE\_REVIEW\_TEMPLATE\_L99.md | PASS/HOLD/FAIL/FROZEN decision | Before next state or approval | HOLD |
| 7 | SMEPLUS\_AI\_EXECUTION\_TEMPLATE\_L99.md | AI agent control | ChatGPT, Claude, Copilot, Make, OpenAI API Agent | HOLD |
| 8 | SMEPLUS\_CLEAN\_ROOM\_LEARNING\_TEMPLATE\_L99.md | Legal-safe learning control | ERP Open Source, dump, source, blueprint study | HOLD |
| 9 | SMEPLUS\_NEXT\_STATE\_HANDOFF\_TEMPLATE\_L99.md | State-to-state transfer | Before moving to the next state | HOLD |
| 10 | SMEPLUS\_DOCUMENT\_CONTROL\_STANDARD\_L99.md | Document governance | Versioning, naming, status, change log | HOLD |

## Template Selection Rule

| Work Type | Required Template |
| --- | --- |
| New governance or standard document | Master Template Standard + Document Control Standard |
| Evidence collection | Evidence Register Template |
| Requirement, FDS, design, build, QA mapping | Traceability Matrix Template |
| Approval or gate decision | Gate Review Template |
| AI execution, prompt, analysis, coding support | AI Execution Template |
| Learning from ERP Open Source, dump, source code, blueprint | Clean Room Learning Template |
| Moving from one state to another | Next-State Handoff Template |

## Package Review Checklist

| Review Item | Required Result |
| --- | --- |
| All target files present | Yes |
| No shell scripts included | Yes |
| Markdown only | Yes |
| No auto-approval wording | Yes |
| Commit remains HOLD | Yes |
| Merge remains HOLD | Yes |
| Production remains HOLD | Yes |
| Clean Room rule included | Yes |
