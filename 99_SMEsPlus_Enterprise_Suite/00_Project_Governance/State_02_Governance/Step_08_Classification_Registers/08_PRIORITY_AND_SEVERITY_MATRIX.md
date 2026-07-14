# 08_PRIORITY_AND_SEVERITY_MATRIX.md

Order: /L99.99 — State 02, Step 08 — Classification Registers
Work Package: WP-08-08 — Priority and Severity Matrix
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Working Branch: claude/state-02-classification-registers-7qwwcy
Prepared By: Claude Code (Preparer / Executor — Responsible role only)
Prepared At: 2026-07-14 (UTC)
Document Status: PREPARED FOR INDEPENDENT REVIEW
Gate Status: HOLD

## 1. Priority Definitions

```text
P0 — Critical blocker (blocks State / Gate)
P1 — High-impact blocker (blocks Step)
P2 — Important non-blocking item
P3 — Administrative or improvement item
```

## 2. Severity Definitions

```text
S0 — State / Gate integrity failure
S1 — Major governance failure
S2 — Material control weakness
S3 — Minor control or documentation issue
S4 — Observation or improvement
```

## 3. Priority Handling Matrix

| Priority | Escalation Time (from identification) | Responsible Authority | Evidence Requirement | Gate Impact |
|---|---|---|---|---|
| P0 | Immediate (same day); escalate to Boss within 24h | Owner → Executive Secretary → Boss | E0/E1 evidence + escalation record | Blocking — Gate cannot PASS while open |
| P1 | Within 2 business days | Owner → Executive Secretary | E1 evidence + action record | Blocking for the Step |
| P2 | Within 5 business days | Owner | E1/E2 evidence | Input; non-blocking |
| P3 | Best effort; by milestone 2026-10-31 | Owner | Record | None |

## 4. Severity Handling Matrix

| Severity | Escalation Time | Responsible Authority | Evidence Requirement | Gate Impact |
|---|---|---|---|---|
| S0 | Immediate; Boss notified within 24h | Executive Secretary → Boss | Correction evidence + independent verify | FAIL / FROZEN until corrected |
| S1 | Within 2 business days | Executive Secretary | Correction evidence | Blocking |
| S2 | Within 5 business days | Owner → Executive Secretary | Correction evidence | HOLD |
| S3 | Within milestone window | Owner | Evidence | Input |
| S4 | Logged; no deadline | Owner | Note | None |

## 5. Priority × Severity Combined Matrix

Cell = required response (escalation window / authority / gate effect). "Boss" = escalation
authority; all gate PASS remains a Boss decision supported by independent evidence.

| | S0 | S1 | S2 | S3 | S4 |
|---|---|---|---|---|---|
| **P0** | Immediate; Boss 24h; FROZEN/FAIL until corrected + independent verify | Immediate; Boss 24h; Blocking | Same day; ES; Blocking | Same day; ES; Blocking (P0 dominates) | Same day; ES; Blocking (P0 dominates) |
| **P1** | Immediate; Boss 24h; FAIL until corrected | 2 days; ES; Blocking (Step) | 2 days; ES; Blocking (Step) | 2 days; Owner→ES; Blocking (Step) | 2 days; Owner; Blocking (Step) |
| **P2** | 24h; ES→Boss; HOLD | 2 days; ES; HOLD | 5 days; Owner; Input | 5 days; Owner; Input | 5 days; Owner; Input |
| **P3** | 24h; ES→Boss; HOLD (integrity dominates) | 2 days; ES; Input | 5 days; Owner; Input | milestone; Owner; None | milestone; Owner; None |

Rule: when Priority and Severity disagree, the more restrictive gate effect governs (an
S0 forces at least HOLD even at P3; a P0 forces Blocking even at S4).

## 6. Application to Current State 02 Items

| Item | Priority | Severity | Combined Response |
|---|---|---|---|
| RAID-08-R01 (6 open ACF P0 lines) | P0 | S0 | FROZEN/FAIL until corrected + independently verified; Boss escalation |
| RAID-08-R02 (no named Verifier) | P0 | S1 | Immediate; Boss 24h; Blocking |
| RAID-08-I01 (branch discrepancy) | P1 | S2 | 2 days; ES; Blocking (accept required) |
| RAID-08-A01 (root-standard qualification) | P2 | S3 | 5 days; Owner; Input |

## 7. Control Statement

This matrix defines response and gate effect only. It does not itself declare any Gate
result. Gate PASS remains a Boss decision supported by independent review and verification.
