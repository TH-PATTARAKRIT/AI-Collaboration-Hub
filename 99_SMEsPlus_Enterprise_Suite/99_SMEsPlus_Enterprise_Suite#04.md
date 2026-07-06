#!/usr/bin/env bash

set -e

BASE="99\_SMEsPlus\_Enterprise\_Suite"

mkdir -p "$BASE/07\_Output\_From\_AI"

mkdir -p "$BASE/14\_Claude\_Execution/Task\_Prompts"

mkdir -p "$BASE/04\_Review\_Gates"

cat > "$BASE/14\_Claude\_Execution/Task\_Prompts/ACC-001\_CLAUDE\_REVIEW\_PROMPT.md" <<'EOF'

# ACC-001 Claude Review Prompt

Version: v1.0

Status: Ready for Claude Review

Owner: Functional Specification AI

Target Reviewer: Claude AI

Working Rule: /L99

## Review Target

Please review:

- 02\_Functional\_Design/ACC-001 Accounting Thailand Functional Design Specification Package.md

- 07\_Output\_From\_AI/ACC-001\_GAP\_ANALYSIS.md

- 07\_Output\_From\_AI/ACC-001\_EVIDENCE\_REGISTER.md

- 12\_Traceability/Requirement\_Matrix/ACC-001\_TRACEABILITY\_MATRIX.md

## Review Objectives

1. ตรวจ missing requirement ของ Accounting Thailand

2. ตรวจ VAT / WHT / Tax Invoice / Receipt / Credit Note / Debit Note completeness

3. ตรวจ SaaS alignment

4. ตรวจ Clean Room compliance

5. ตรวจ Evidence status

6. ตรวจ Traceability completeness

7. ตรวจ API / DB / UI mapping gap

8. แนะนำ Reuse / Adapt / New classification

## Required Output

| Finding ID | Area | Finding | Severity | Recommendation | Evidence Status |

|---|---|---|---|---|---|

## Decision

เลือกหนึ่งสถานะ:

- Approved for PMO Review

- Approved with Minor Changes

- Hold for Major Revision

- Reject due to Missing Evidence

EOF

cat > "$BASE/04\_Review\_Gates/ACC-001\_REVIEW\_GATE\_RECORD.md" <<'EOF'

# ACC-001 Review Gate Record

Version: v1.0

Status: Review Required

Owner: PMO / Functional Specification AI

Working Rule: /L99

## Gate

ACC-001 Accounting Thailand Functional Specification Review Gate

## Gate Checklist

| Item | Status |

|---|---|

| FDS Package Created | Done |

| Gap Analysis Created | Pending Upload |

| Evidence Register Created | Pending Upload |

| Traceability Matrix Created | Pending Upload |

| Claude Review Prompt Created | Draft Completed |

| Claude Review Completed | Pending |

| PMO Review Completed | Pending |

| Boss Approval | Pending |

## Current Decision

Status: HOLD FOR REVIEW

Reason: Claude Review and PMO Review are not completed yet.

## Next Action

Submit ACC-001 package to Claude AI review.

EOF

cat > "$BASE/07\_Output\_From\_AI/ACC-001\_NEXT\_PROCESS\_CHECKLIST\_STATUS.md" <<'EOF'

# ACC-001 Next Process Checklist Status

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

Working Rule: /L99

## Checklist

| Item | Status |

|---|---|

| ตรวจ GitHub ล่าสุดก่อนดำเนินการ | Done |

| ไม่สร้าง ACC-001 FDS ซ้ำ | Done |

| ใช้ path เดิมของ Repository | Done |

| Claude Review Prompt | Draft Completed |

| Review Gate Record | Draft Completed |

| Current Gate | Review Required |

| Next Step | Claude Review |

## Files Created

| Path | File |

|---|---|

| 14\_Claude\_Execution/Task\_Prompts | ACC-001\_CLAUDE\_REVIEW\_PROMPT.md |

| 04\_Review\_Gates | ACC-001\_REVIEW\_GATE\_RECORD.md |

| 07\_Output\_From\_AI | ACC-001\_NEXT\_PROCESS\_CHECKLIST\_STATUS.md |

EOF

echo "ACC-001 next process package created successfully."