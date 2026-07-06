#!/usr/bin/env bash

set -e

BASE="99\_SMEsPlus\_Enterprise\_Suite"

mkdir -p "$BASE/04\_Review\_Gates"

mkdir -p "$BASE/07\_Output\_From\_AI"

mkdir -p "$BASE/08\_Testing\_Evidence"

cat > "$BASE/04\_Review\_Gates/ACC-001\_BOSS\_DECISION\_REQUEST.md" <<'EOF'

# ACC-001 Boss Decision Request

Version: v1.0

Status: Decision Required

Owner: PMO AI / Functional Specification AI

Working Rule: /L99

## Purpose

ใช้ขอการตัดสินใจจาก Boss สำหรับ Scope สำคัญของ ACC-001 ก่อนปิด Gap และเข้าสู่ Enterprise FDS Merge

## Decision Items

| Decision ID | Topic | Options | Recommended | Decision |

|---|---|---|---|---|

| DEC-ACC-001 | e-Tax / e-Receipt Phase | Phase 1 / Phase 2 | Phase 2 | Pending |

| DEC-ACC-002 | Currency Scope | THB only / Multi-currency | THB only for Phase 1 | Pending |

| DEC-ACC-003 | Cost Center / Project Accounting | Phase 1 / Phase 2 | Phase 2 | Pending |

| DEC-ACC-004 | Bank Integration | Import Statement / Direct API | Import Statement for Phase 1 | Pending |

| DEC-ACC-005 | Tax Report Export | PDF / Excel / CSV / Revenue Dept format | Excel + CSV first | Pending |

## Decision Rule

หากไม่มี decision evidence รายการที่เกี่ยวข้องต้องคงสถานะ HOLD

EOF

cat > "$BASE/08\_Testing\_Evidence/ACC-001\_BOSS\_DECISION\_EVIDENCE\_RECORD.md" <<'EOF'

# ACC-001 Boss Decision Evidence Record

Version: v1.0

Status: Waiting for Decision

Owner: PMO AI

Working Rule: /L99

| Evidence ID | Decision ID | Evidence Required | Status |

|---|---|---|---|

| EV-DEC-ACC-001 | DEC-ACC-001 | Boss decision on e-Tax/e-Receipt phase | Missing |

| EV-DEC-ACC-002 | DEC-ACC-002 | Boss decision on currency scope | Missing |

| EV-DEC-ACC-003 | DEC-ACC-003 | Boss decision on cost center/project accounting | Missing |

| EV-DEC-ACC-004 | DEC-ACC-004 | Boss decision on bank integration scope | Missing |

| EV-DEC-ACC-005 | DEC-ACC-005 | Boss decision on tax report export format | Missing |

## Evidence Rule

No Evidence = No Progress

EOF

cat > "$BASE/07\_Output\_From\_AI/ACC-001\_NEXT\_PROCESS\_009\_CHECKLIST\_STATUS.md" <<'EOF'

# ACC-001 Next Process 009 Checklist Status

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

Working Rule: /L99

| Item | Status |

|---|---|

| ตรวจ Repository ก่อนดำเนินการ | Done |

| ไม่สร้าง FDS ซ้ำ | Done |

| ใช้ path เดิม | Done |

| Boss Decision Request | Draft Completed |

| Boss Decision Evidence Record | Draft Completed |

| Current Gate | HOLD FOR BOSS DECISION / REVIEW EVIDENCE |

| Next Step | Boss decision + Claude/Architecture Review execution |

## Files Created

| Path | File |

|---|---|

| 04\_Review\_Gates | ACC-001\_BOSS\_DECISION\_REQUEST.md |

| 08\_Testing\_Evidence | ACC-001\_BOSS\_DECISION\_EVIDENCE\_RECORD.md |

| 07\_Output\_From\_AI | ACC-001\_NEXT\_PROCESS\_009\_CHECKLIST\_STATUS.md |

EOF

echo "ACC-001 boss decision scope package created successfully."