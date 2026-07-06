#!/usr/bin/env bash

set -e

BASE="99\_SMEsPlus\_Enterprise\_Suite"

mkdir -p "$BASE/04\_Review\_Gates"

mkdir -p "$BASE/15\_ChatGPT\_Review/Architecture\_Review"

mkdir -p "$BASE/07\_Output\_From\_AI"

cat > "$BASE/15\_ChatGPT\_Review/Architecture\_Review/ACC-001\_ARCHITECTURE\_REVIEW\_PROMPT.md" <<'EOF'

# ACC-001 Architecture Review Prompt

Version: v1.0

Status: Ready for Architecture Review

Owner: Functional Specification AI

Reviewer: ChatGPT / Liza

Working Rule: /L99

## Review Target

- 02\_Functional\_Design/ACC-001 Accounting Thailand Functional Design Specification Package.md

- 07\_Output\_From\_AI/ACC-001\_GAP\_ANALYSIS.md

- 07\_Output\_From\_AI/ACC-001\_EVIDENCE\_REGISTER.md

- 12\_Traceability/Requirement\_Matrix/ACC-001\_TRACEABILITY\_MATRIX.md

- 04\_Review\_Gates/ACC-001\_REVIEW\_GATE\_RECORD.md

## Review Objectives

1. ตรวจ SaaS alignment

2. ตรวจ multi-tenant / tenant isolation

3. ตรวจ RBAC / permission scope

4. ตรวจ API-first readiness

5. ตรวจ DB mapping sufficiency

6. ตรวจ audit / evidence coverage

7. ตรวจ integration readiness

8. ตรวจว่าไม่ซ้ำกับ SaaS Foundation

## Required Output

| Finding ID | Area | Finding | Severity | Recommendation | Gate Impact |

|---|---|---|---|---|---|

## Decision

- Pass to PMO Review

- Pass with Minor Changes

- Hold for Architecture Gap

- Reject due to Structural Conflict

EOF

cat > "$BASE/04\_Review\_Gates/ACC-001\_PMO\_REVIEW\_CHECKLIST.md" <<'EOF'

# ACC-001 PMO Review Checklist

Version: v1.0

Status: Review Required

Owner: PMO AI

Working Rule: /L99

| Gate Item | Status |

|---|---|

| FDS Package Exists | Done |

| Gap Analysis Exists | Pending Verification |

| Evidence Register Exists | Pending Verification |

| Traceability Matrix Exists | Pending Verification |

| Claude Review Prompt Exists | Pending Verification |

| Architecture Review Prompt Exists | Draft Completed |

| No Duplicate Check | Done |

| SaaS Foundation Reuse Check | Required |

| Evidence Completeness Check | Required |

| Boss Approval | Pending |

## Current Gate

PMO Review Required

## Decision

HOLD until Claude Review, Architecture Review, and PMO Review are completed.

EOF

cat > "$BASE/07\_Output\_From\_AI/ACC-001\_NEXT\_PROCESS\_002\_CHECKLIST\_STATUS.md" <<'EOF'

# ACC-001 Next Process 002 Checklist Status

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

Working Rule: /L99

| Item | Status |

|---|---|

| ตรวจ Repository ล่าสุด | Done |

| ไม่สร้าง FDS ซ้ำ | Done |

| ใช้ path เดิม | Done |

| Architecture Review Prompt | Draft Completed |

| PMO Review Checklist | Draft Completed |

| Current Gate | Review Required |

| Next Step | Claude Review + Architecture Review + PMO Review |

## Files Created

| Path | File |

|---|---|

| 15\_ChatGPT\_Review/Architecture\_Review | ACC-001\_ARCHITECTURE\_REVIEW\_PROMPT.md |

| 04\_Review\_Gates | ACC-001\_PMO\_REVIEW\_CHECKLIST.md |

| 07\_Output\_From\_AI | ACC-001\_NEXT\_PROCESS\_002\_CHECKLIST\_STATUS.md |

EOF

echo "ACC-001 PMO + Architecture Review package created successfully."