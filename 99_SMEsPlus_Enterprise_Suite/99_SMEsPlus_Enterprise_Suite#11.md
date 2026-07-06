#!/usr/bin/env bash

set -e

BASE="99\_SMEsPlus\_Enterprise\_Suite"

mkdir -p "$BASE/04\_Review\_Gates"

mkdir -p "$BASE/07\_Output\_From\_AI"

mkdir -p "$BASE/08\_Testing\_Evidence"

mkdir -p "$BASE/12\_Traceability/Requirement\_Matrix"

cat > "$BASE/07\_Output\_From\_AI/ACC-001\_GAP\_CLOSURE\_ACTION\_PLAN.md" <<'EOF'

# ACC-001 Gap Closure Action Plan

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI / PMO AI

Working Rule: /L99

## Purpose

ใช้กำหนดแผนปิด Gap ของ ACC-001 ก่อนเข้าสู่ Enterprise FDS Merge

## Gap Closure Plan

| Gap ID | Gap | Closure Action | Owner | Evidence Required | Status |

|---|---|---|---|---|---|

| GAP-ACC-001 | VAT/WHT legal detail pending | Accounting/Legal review | Accounting Owner | Legal review note | Open |

| GAP-ACC-002 | e-Tax phase undefined | Boss phase decision | Boss | Approval note | Open |

| GAP-ACC-003 | Bank integration undefined | Define Phase 1 bank scope | Finance Owner | Scope decision | Open |

| GAP-ACC-004 | Currency scope undefined | Confirm THB vs multi-currency | Boss / Finance Owner | Scope decision | Open |

| GAP-ACC-005 | Cost center phase undefined | Confirm project/cost center phase | Finance Owner | Scope decision | Open |

| GAP-ACC-006 | Tax report export format undefined | Define export format | Accounting Owner | Report spec note | Open |

| GAP-ACC-007 | Claude review missing | Execute Claude Review | Claude AI | Review result | Pending |

## Closure Rule

ทุก Gap ต้องมี owner, evidence และ decision ก่อนปรับสถานะเป็น Closed

EOF

cat > "$BASE/04\_Review\_Gates/ACC-001\_GAP\_CLOSURE\_GATE.md" <<'EOF'

# ACC-001 Gap Closure Gate

Version: v1.0

Status: HOLD

Owner: PMO AI

Working Rule: /L99

## Gate Checklist

| Item | Status |

|---|---|

| Gap Closure Action Plan | Draft Completed |

| Legal / Accounting Review | Pending |

| Boss Scope Decisions | Pending |

| Claude Review | Pending |

| Architecture Review | Pending |

| PMO Consolidation | Pending |

## Gate Decision

HOLD

## Reason

ACC-001 ยังมี Open Gap ที่ต้องมี evidence ก่อนเข้าสู่ Enterprise FDS Merge

EOF

cat > "$BASE/08\_Testing\_Evidence/ACC-001\_GAP\_CLOSURE\_EVIDENCE\_LOG.md" <<'EOF'

# ACC-001 Gap Closure Evidence Log

Version: v1.0

Status: Open

Owner: PMO AI / QA AI

Working Rule: /L99

| Evidence ID | Related Gap | Evidence Name | Status | Owner |

|---|---|---|---|---|

| EV-GAP-ACC-001 | GAP-ACC-001 | VAT/WHT Legal Review Note | Missing | Accounting Owner |

| EV-GAP-ACC-002 | GAP-ACC-002 | e-Tax Phase Decision | Missing | Boss |

| EV-GAP-ACC-003 | GAP-ACC-003 | Bank Integration Scope Decision | Missing | Finance Owner |

| EV-GAP-ACC-004 | GAP-ACC-004 | Currency Scope Decision | Missing | Boss / Finance Owner |

| EV-GAP-ACC-005 | GAP-ACC-005 | Cost Center Phase Decision | Missing | Finance Owner |

| EV-GAP-ACC-006 | GAP-ACC-006 | Tax Report Export Format Decision | Missing | Accounting Owner |

| EV-GAP-ACC-007 | GAP-ACC-007 | Claude Review Result | Missing | Claude AI |

EOF

cat > "$BASE/12\_Traceability/Requirement\_Matrix/ACC-001\_GAP\_TO\_REQUIREMENT\_MAP.md" <<'EOF'

# ACC-001 Gap to Requirement Map

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

Working Rule: /L99

| Gap ID | Related FR | Related BR | Related API / DB / UI | Status |

|---|---|---|---|---|

| GAP-ACC-001 | FR-ACC-009, FR-ACC-010, FR-ACC-011, FR-ACC-012 | BR-ACC-003, BR-ACC-007, BR-ACC-008 | TaxInvoice, WHTCertificate, VAT Report | Open |

| GAP-ACC-002 | FR-ACC-011 | BR-ACC-003 | TaxInvoice / Receipt | Open |

| GAP-ACC-003 | FR-ACC-013, FR-ACC-018 | BR-ACC-010 | BankAccount, IntegrationLog | Open |

| GAP-ACC-004 | FR-ACC-001, FR-ACC-015 | BR-ACC-010 | AccountingPeriod, Reports | Open |

| GAP-ACC-005 | FR-ACC-015, FR-ACC-019 | BR-ACC-010 | Reports, TenantScope | Open |

| GAP-ACC-006 | FR-ACC-009, FR-ACC-010, FR-ACC-015 | BR-ACC-007, BR-ACC-008 | VAT/WHT/Financial Reports | Open |

| GAP-ACC-007 | All | All | All | Pending |

EOF

cat > "$BASE/07\_Output\_From\_AI/ACC-001\_NEXT\_PROCESS\_007\_CHECKLIST\_STATUS.md" <<'EOF'

# ACC-001 Next Process 007 Checklist Status

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

Working Rule: /L99

| Item | Status |

|---|---|

| ตรวจ Repository ก่อนดำเนินการ | Done |

| ไม่สร้าง FDS ซ้ำ | Done |

| ใช้ path เดิม | Done |

| Gap Closure Action Plan | Draft Completed |

| Gap Closure Gate | Draft Completed |

| Gap Closure Evidence Log | Draft Completed |

| Gap to Requirement Map | Draft Completed |

| Current Gate | HOLD FOR GAP CLOSURE |

| Next Step | Collect decisions and review evidence |

## Files Created

| Path | File |

|---|---|

| 07\_Output\_From\_AI | ACC-001\_GAP\_CLOSURE\_ACTION\_PLAN.md |

| 04\_Review\_Gates | ACC-001\_GAP\_CLOSURE\_GATE.md |

| 08\_Testing\_Evidence | ACC-001\_GAP\_CLOSURE\_EVIDENCE\_LOG.md |

| 12\_Traceability/Requirement\_Matrix | ACC-001\_GAP\_TO\_REQUIREMENT\_MAP.md |

| 07\_Output\_From\_AI | ACC-001\_NEXT\_PROCESS\_007\_CHECKLIST\_STATUS.md |

EOF

echo "ACC-001 gap closure execution package created successfully."