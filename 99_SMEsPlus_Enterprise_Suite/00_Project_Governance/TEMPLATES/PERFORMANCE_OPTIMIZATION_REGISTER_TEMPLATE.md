# PERFORMANCE OPTIMIZATION REGISTER TEMPLATE

Template ID: SMEPLUS-TPL-PERF-OPT-001
Version: v1.0
Status: BOSS APPROVED / MANDATORY TEMPLATE
Effective Date: 2026-08-30

## Register Columns

| Field | Required |
|---|---|
| Finding ID | YES |
| Date / Build / Commit | YES |
| Team / Gate Source | YES |
| Module / Domain | YES |
| Screen / API / Job / Flow | YES |
| Test ID / Matrix Version | YES where applicable |
| Environment | YES |
| Dataset / Workload Profile | YES |
| Concurrency | YES where applicable |
| Performance Budget ID | YES |
| Target Metric | YES |
| Target / Hard Ceiling | YES |
| p50 | YES where statistically meaningful |
| p95 | YES where statistically meaningful |
| p99 | YES where statistically meaningful |
| Max | YES for critical flows where required |
| Throughput | YES where applicable |
| Error / Timeout Rate | YES where applicable |
| Baseline Version | YES |
| Allowed Regression Threshold | YES |
| Actual Result | YES |
| Variance | YES |
| Severity / Business Impact | YES |
| Bottleneck Classification | YES |
| Optimization Required | YES |
| Assignee | YES; `UNASSIGNED` is a Red Flag |
| Due Date | YES; `TBD` is a Red Flag |
| Remediation / Optimization Action | YES when required |
| Before Evidence | YES |
| After Evidence | YES when remediated |
| Team D Regression Result | YES where applicable |
| IDTM Retest Result | YES where applicable |
| IESA Disposition | YES where applicable |
| Boss Ruling | YES when risk acceptance / exception is required |
| Final Status | YES |

## Standard Status

- OPEN
- ANALYSIS REQUIRED
- OPTIMIZATION REQUIRED
- IN REMEDIATION
- READY FOR REGRESSION
- READY FOR IDTM RETEST
- PERFORMANCE WITHIN BUDGET
- PERFORMANCE REGRESSION FOUND
- BOTTLENECK FOUND
- PERFORMANCE GATE HOLD
- RISK ACCEPTANCE REQUIRED
- CLOSED BY EVIDENCE

## Core Rule

A finding is not closed because code changed. Closure requires before/after measurable evidence and the applicable regression/retest evidence.

**No Performance Evidence = No Performance Progress.**
